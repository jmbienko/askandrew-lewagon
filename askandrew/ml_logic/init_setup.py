from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os
import openai
from askandrew.params import persist_directory

def database_loading():
    embedding = OpenAIEmbeddings()
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    return vectordb
