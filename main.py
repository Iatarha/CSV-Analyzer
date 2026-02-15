import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI

def main():
    load_dotenv()
    st.set_page_config(page_title="AI CSV Analyzer", layout="wide")
    st.header("📊 AI CSV Analyzer with Cleaning, Summary & Graphs")

    # --- Upload CSV ---
    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if user_csv is not None:
        # --- Read CSV ---
        df = pd.read_csv(user_csv)

        st.subheader("Preview of Uploaded Data")
        st.dataframe(df.head())

        # --- Automatic Null Handling ---
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        non_numeric_cols = df.select_dtypes(exclude='number').columns.tolist()

        for col in numeric_cols:
            df[col].fillna(df[col].median(), inplace=True)
        for col in non_numeric_cols:
            if not df[col].mode().empty:
                df[col].fillna(df[col].mode()[0], inplace=True)
            else:
                df[col].fillna("Unknown", inplace=True)

        st.markdown("✅ Null values automatically handled using best practices.")

        # --- Toggle buttons ---
        if "show_summary" not in st.session_state:
            st.session_state.show_summary = False
        if "show_graphs" not in st.session_state:
            st.session_state.show_graphs = False

        if st.button("📄 Show/Hide Statistical Summary"):
            st.session_state.show_summary = not st.session_state.show_summary
        if st.button("📊 Show/Hide Automatic Graphs"):
            st.session_state.show_graphs = not st.session_state.show_graphs

        # --- Summary Section ---
        if st.session_state.show_summary:
            st.subheader("Statistical Summary")
            summary_df = df.describe().T
            st.dataframe(summary_df)

            st.markdown("**Null Values per Column (After Cleaning)**")
            st.dataframe(df.isnull().sum())

            # Download summary
            csv_bytes = summary_df.to_csv().encode()
            st.download_button(
                label="Download Statistical Summary CSV",
                data=csv_bytes,
                file_name="statistical_summary.csv",
                mime="text/csv"
            )

        # --- Graphs Section ---
        if st.session_state.show_graphs and numeric_cols:
            st.subheader("Automatic Plots for Numeric Columns")

            for col in numeric_cols:
                st.markdown(f"**Column: {col}**")
                
                # Histogram
                fig, ax = plt.subplots()
                ax.hist(df[col], bins=10, color='skyblue', edgecolor='black')
                ax.set_title(f"Histogram of {col}")
                st.pyplot(fig)

                buf = BytesIO()
                fig.savefig(buf, format="png")
                buf.seek(0)
                st.download_button(
                    label=f"Download Histogram of {col}",
                    data=buf,
                    file_name=f"histogram_{col}.png",
                    mime="image/png"
                )
                plt.close(fig)

                # Boxplot
                fig, ax = plt.subplots()
                ax.boxplot(df[col])
                ax.set_title(f"Boxplot of {col}")
                st.pyplot(fig)

                buf = BytesIO()
                fig.savefig(buf, format="png")
                buf.seek(0)
                st.download_button(
                    label=f"Download Boxplot of {col}",
                    data=buf,
                    file_name=f"boxplot_{col}.png",
                    mime="image/png"
                )
                plt.close(fig)

            # Scatter plots for numeric pairs
            if len(numeric_cols) >= 2:
                st.subheader("Scatter Plots")
                for i in range(len(numeric_cols)):
                    for j in range(i + 1, len(numeric_cols)):
                        x_col = numeric_cols[i]
                        y_col = numeric_cols[j]
                        fig, ax = plt.subplots()
                        ax.scatter(df[x_col], df[y_col])
                        ax.set_xlabel(x_col)
                        ax.set_ylabel(y_col)
                        ax.set_title(f"{y_col} vs {x_col}")
                        st.pyplot(fig)

                        buf = BytesIO()
                        fig.savefig(buf, format="png")
                        buf.seek(0)
                        st.download_button(
                            label=f"Download Scatter Plot: {y_col} vs {x_col}",
                            data=buf,
                            file_name=f"scatter_{x_col}_vs_{y_col}.png",
                            mime="image/png"
                        )
                        plt.close(fig)

        # --- AI Agent Section ---
        user_question = st.text_input("Ask a question about your CSV:")
        if user_question:
            # Save cleaned CSV to BytesIO
            temp_csv = BytesIO()
            df.to_csv(temp_csv, index=False)
            temp_csv.seek(0)

            llm = OpenAI(temperature=0)
            agent = create_csv_agent(
                llm,
                temp_csv,
                verbose=True,
                allow_dangerous_code=True
            )
            response = agent.run(user_question)
            st.markdown("### 🧠 AI Response")
            st.write(response)


if __name__ == "__main__":
    main()
