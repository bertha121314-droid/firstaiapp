
#run in terminal - streamlit run tweetapp.py
#from pathlib import Path
#from dotenv import load_dotenv  # will be grey until used
#load_dotenv(dotenv_path=Path(__file__).parent / ".env")

#Use Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

import os
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])
# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model | StrOutputParser()
# print(tweet_chain.invoke({"number" : 2, "topic" : "Wars in Middle East"}))



st.header("Tweet Generator")
st.subheader("Generate Tweets using Generative AI")
topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)
if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
    st.write(tweets)
