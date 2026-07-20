import streamlit as st
from automation.cleaner import clean_code
from parser.pdf_parser import extract_pdf_text
from chunking.splitter import split_text
from embeddings.embedding import create_embeddings
from vectordb.chroma_db import store_embeddings
from retrieval.retriever import retrieve_chunks

from llm.prompt import build_prompt
from llm.generator import generate_test_cases

from automation.generator import generate_selenium_script
from automation.executor import execute_test

st.title("AI-Powered Test Automation Framework")

st.write(
    "Upload requirement documents and generate automated test cases"
)


uploaded_file = st.file_uploader(
    "Upload Requirement Document",
    type=["pdf", "docx", "txt"]
)


if uploaded_file:


    if st.button("Generate Test Cases"):


        # 1. Extract text
        text = extract_pdf_text(
            uploaded_file
        )


        st.subheader(
            "Extracted Requirement"
        )

        st.write(text)



        # 2. Chunking

        chunks = split_text(text)



        # 3. Embeddings + Vector DB

        embeddings = create_embeddings(chunks)

        store_embeddings(
            chunks,
            embeddings,
            uploaded_file.name
        )



        # 4. Retrieve

        results = retrieve_chunks(
            "Generate test cases"
        )


        context = "\n".join(
            results["documents"][0]
        )



        # 5. LLM

        prompt = build_prompt(
            context
        )


        test_cases = generate_test_cases(
            prompt
        )



        st.subheader(
            "Generated Test Cases"
        )


        st.code(test_cases)



        # Save for next button

        st.session_state["test_cases"] = test_cases



if "test_cases" in st.session_state:


    if st.button(
        "Generate Selenium Script"
    ):


        selenium_code = generate_selenium_script(
            st.session_state["test_cases"]
        )

        selenium_code = clean_code(
            selenium_code
        )

        st.subheader(
            "Generated Selenium Code"
        )


        st.code(
            selenium_code,
            language="python"
        )
        print("===== SELENIUM CODE =====")
        print(selenium_code)
        print("==========================")


        st.session_state["selenium_code"] = selenium_code



if "selenium_code" in st.session_state:

    if st.button("Run Test"):

        selenium_code = generate_selenium_script(
            st.session_state["test_cases"]
        )

        result = execute_test(
            selenium_code
        )

        st.subheader(
            "Execution Result"
        )

        st.success(result)