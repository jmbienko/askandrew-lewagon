from langchain_community.vectorstores import Chroma
#from langchain_community import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
#from langchain.vectorstores import Chroma
import os
#from params.params import openai_api_key
import openai
from askandrew.params import persist_directory

def database_loading():
    embedding = OpenAIEmbeddings()
    #openai.api_key = openai_api_key

    openai.api_key = os.environ.get('OPENAI_API_KEY')

    ###!!!!!remember to change it to absolute path!!!
    #persist_directory = "/home/martina/code/jmbienko/askandrew-lewagon/askandrew/chroma"

    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    #vectordb.get()
 #   print(f"succesfully loaded vectordb with {vectordb._collection.count()} embeddings")

    return vectordb


    #sample_items = vectordb._collection.count()
    #print(sample_items)
