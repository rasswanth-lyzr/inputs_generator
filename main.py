import streamlit as st
from lyzr import ChatBot
from dotenv import load_dotenv
import os
from lyzr_functions import explain_image, generate_sample_inputs

load_dotenv()

# LOAD OUR API KEY
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def initialize_chatbot():
    # To connect an external Weaviate cluster for the Chatbot
    vector_store_params = {
        "vector_store_type": "WeaviateVectorStore",
        "url": WEAVIATE_URL,
        "api_key": WEAVIATE_API_KEY,
        "index_name": "IndexName2"
    }

    chatbot = ChatBot.txt_chat(
        input_files=["fields.txt"],
        vector_store_params=vector_store_params
    )

    return chatbot

# Generate sample inputs using Automata
@st.cache_data
def generate_information_file():
    # IMAGE FILE PATH
	image_path = "volunteer form.png"
	image_result = explain_image(image_path, OPENAI_API_KEY)
	generated_fields_output = generate_sample_inputs(image_result, OPENAI_API_KEY)

	with open("fields.txt", "w") as file:
		# Write the text to the file
		file.write(image_result + "\n")
		file.write(generated_fields_output + "\n")      
     
st.text("Initializing the Chatbot...")
generate_information_file()

# initizlize the chatbot to answer questions
question = st.text_input("Ask a question about the Webpage:")
if st.button("Get Answer"):
    st.text("Processing...")
    chatbot = initialize_chatbot()
    if chatbot:
        response = chatbot.chat(question)
        st.text("Answer:")
        st.write(response.response)