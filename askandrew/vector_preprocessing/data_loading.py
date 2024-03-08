from langchain.document_loaders import TextLoader
import os #to be able to create the for loop to loop through the documents
from askandrew.params import *


#loading all txt.files into "loaded_text"

def file_loading():

    docs_path = os.path.join(local_directory, "docs/")
    loaded_files = []

    # List all files in the docs directory
    for filename in os.listdir(docs_path):
        # Check if the file is a .txt file
        if filename.endswith(".txt"):
            # Construct the full path and add a TextLoader object for it to loaded_files
            full_path = os.path.join(docs_path, filename)
            loaded_files.append(TextLoader(full_path))

    #unloading the content + metadata into the list
    loaded_content = []
    for file in loaded_files:
        loaded_content.extend(file.load())

    return loaded_content
