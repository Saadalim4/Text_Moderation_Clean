import streamlit as st
import requests

st.title("🛡️ Text Moderation Assistant")

texts = st.text_area("Enter text(s), one per line:")
language = st.selectbox("Language", ["en", "es"])
sensitivity = st.select_slider("Sensitivity", options=["strict", "moderate", "lenient"])

if st.button("Moderate"):
    input_texts = [line for line in texts.split("\n") if line.strip()]
    try:
        response = requests.post(
            "http://localhost:8000/moderate",
            json={"texts": input_texts, "language": language, "sensitivity": sensitivity},
            timeout=10  # Avoid hanging
        )
        
        # Check if response is valid JSON
        if response.status_code == 200:
            try:
                results = response.json().get("results", [])
                for res in results:
                    st.markdown("---")
                    st.write(f"*Original:* {res.get('original', 'N/A')}")
                    st.write(f"*Flagged:* {res.get('classification', '').lower() in ['flagged', 'offensive']}")
                    st.write(f"*Reason:* {res.get('reason', 'No reason provided')}")
                    st.write(f"*Edited:* {res.get('edited', 'No edits made')}")
            except ValueError as e:
                st.error(f"Failed to parse JSON: {e}\nResponse: {response.text}")
        else:
            st.error(f"Server error: {response.status_code}\n{response.text}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")