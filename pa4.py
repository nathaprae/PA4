import streamlit as st
import openai
import pandas as pd


st.sidebar.title("API Key Here!")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

st.title("Informal to Formal Text Converter")
st.write("We will convert a social media message to a formal version with slang explanations for you!")

input_text = st.text_area("Enter your social media message here:")

if st.button("Convert"):
    if not api_key:
        st.error("Please provide your API Key.")
    elif not input_text.strip():
        st.error("Please enter a message.")
    else:
        openai.api_key = api_key
        response = openai.Completion.create(
            model = "gpt-4", 
            prompt = input_text,                
            max_tokens = 500
        )
        formal_text = response['choices'][0]['text'].strip()

        st.subheader("Formal Version:")            
        st.write(formal_text)

        slang_list = []
        for line in formal_text.splitlines():
            if ":" in line and "Word" not in line:
                word, meaning = line.split(":", 1)                    
                slang_list.append({"Word": word.strip(), "Meaning": meaning.strip()})

        if slang_list:
            st.subheader("Slang and Meanings:")
            df = pd.DataFrame(slang_list)
            st.dataframe(df)
        else:
            st.write("No slang words detected.")

   
