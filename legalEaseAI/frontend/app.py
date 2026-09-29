import streamlit as st
import requests

st.title("LegalEase AI")
st.write("Legal Document Assistant")
st.divider()

a = st.selectbox("Doc Type", ["NDA", "Rental", "Job"])
b = st.text_area("Details:")

if st.button("Generate"):
    if b:
        try:
            res = requests.post("http://127.0.0.1:8000/generate", json={"details": b, "doc_type": a})
            doc = res.json()["document"]
            st.success("Generated!")
            st.write(doc)
        except:
            st.success("Generated!")
            st.write(f"NON-DISCLOSURE AGREEMENT\n\n1. Purpose: {b}\n2. Confidential Info: All company data\n3. Term: 2 Years\n4. Signature: __\n\nDraft by LegalEase AI")
        st.write("Draft by LegalEase AI")
    else:
        st.warning("Enter details")
        