from langchain_community.vectorstores import Chroma

# Assuming you're loading a pre-existing ChromaDB from a specific directory
vectordb = Chroma(persist_directory="embeddings/")

# Example usage: Querying the database (the specifics would depend on Chroma's API)
# For demonstration, let's say we want to check the number of items/documents
# This assumes `vectordb` has a method to report such information directly
# Note: Replace `count()` with the appropriate method or property as per Chroma's documentation
print(vectordb._collection.count())










#from askandrew.params import *
#from langchain.vectorstores import Chroma  # Assuming Chroma is the correct class name

#import chromadb

# Assuming 'embedding' is a function you have defined elsewhere that you want to pass as an argument
# Make sure the 'embedding' function is correctly defined/imported

# Load the pre-processed vectorDB (Chroma)
# Correcting the path to use forward slashes and fixing the syntax for embedding_function argument
#vectordb = Chroma(persist_directory="embeddings/", embedding_function=embedding)

# Assuming _collection is a property of the Chroma class that exposes some sort of database or collection
#print(vectordb._collection.count())




#persistent_client = chromadb.PersistentClient()
#collection = persistent_client.get_or_create_collection("collection_name")
#collection.add(ids=["1", "2", "3"], documents=["a", "b", "c"])
#vectordb = chroma(
#    client=persistent_client,
#   collection_name="collection_name",
#   embedding_function=embedding_function,
#)
#print("There are", vectordb._collection.count(), "in the collection")





'''

DO WE STILL NEED THIS?

sys.path.append('../..')

#loading dotenv !!!!!! remember to adjust it with local .envrc file!!!!!!
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


'''
