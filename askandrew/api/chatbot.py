from askandrew.ml_logic.init_setup import database_loading
from askandrew.ml_logic.llm_setup import start_llm
from askandrew.ml_logic.question_answer import user_input, answer_ss, answer_mmr, llm_based_answer
from askandrew.api.api import *
import warnings

def chatbot(question):

    from langchain_openai import OpenAIEmbeddings

    warnings.filterwarnings("ignore", category=DeprecationWarning, message="The function `__call__` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.")

    vectordb = database_loading() #returns vectordb

    qa_chain_mr = start_llm(vectordb)

    output = answer_mmr(vectordb, question)

    response = llm_based_answer(output, qa_chain_mr, question)
