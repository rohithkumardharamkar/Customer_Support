import streamlit as st
from workflow.graph import workflow
st.set_page_config(page_title="Customer Support Assistant",)

st.title("Customer Support Assistant")
st.write("Analyze customer complaints using AI workflows.")

review = st.text_area("Enter Customer Complaint")

if st.button("Analyze Complaint"):
    if review.strip() == "":
        st.warning("Please enter a complaint.")
    else:
        initial_state = {"review": review}
        result = workflow.invoke(initial_state)
        st.success(result["sentiment"])

        if result["sentiment"] == "negative":
            st.subheader("Diagnosis")
            st.json(result["diagnosis"])

        st.write(result["response"])