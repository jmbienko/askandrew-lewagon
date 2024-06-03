from askandrew.ml_logic.init_setup import *

def test_function():
    print("test")



# user - question - for now: set as a variable, should be changed to input function later
def user_input():

    from langchain_community.chat_models import ChatOpenAI

    question = input("Please enter your question:\n\n\n")

    return question


# Similarity-Search-Answer: provide k content chunks form vectordb, using similarity search method

def answer_ss(vectordb, question):

    from langchain_community.chat_models import ChatOpenAI

    output = vectordb.similarity_search(question,k=3)

    return output

# Maximum-Marginal-Relevance-Answer: provide k content chunks form vectordb, using similarity search method
def answer_mmr(vectordb, question):

    from langchain_community.chat_models import ChatOpenAI

    output = vectordb.max_marginal_relevance_search(question,k=4,fetch_k=5)

    return output


def llm_based_answer(output, qa_chain_mr, question):

    from langchain_community.chat_models import ChatOpenAI

    # putting this so the wait does not take too long

    print("that is an interesting question, let me think...\n\n")

    # creating a list with the sources used, that should be printed
    sources = []
    for item in output:
        if item.metadata['source'] in sources:
            continue
        else:
            sources.append(item.metadata['source'])

    #creating the result - this will take a while
    result = qa_chain_mr({"query": question})

    #printing the result + sources
    print(f"You have asked the following question: '{result['query']}' \n\n {result['result']} \n\n If you want to know more I would recommend you to check this out: {sources}")

    return result
