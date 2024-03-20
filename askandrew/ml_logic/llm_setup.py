from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from askandrew.ml_logic.init_setup import *



### VECTORDB - SHOULD I CALL IT BEFOIRE I CAN USE IT? ###

def start_llm(vectordb):

    from langchain_community.chat_models import ChatOpenAI

    # chosing the llm model
    llm_name = "gpt-3.5-turbo-0125"
    llm = ChatOpenAI(model_name=llm_name, temperature=0)

    # setting prompt parameters
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    #using a "refine" to work on the k=n inputs and building on them after each other
    qa_chain_mr = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    chain_type="stuff",

    #for a quicker result: change to
    #chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    return_source_documents=True)

 #   print("sucesfully ran through llm_setup")

    return qa_chain_mr
