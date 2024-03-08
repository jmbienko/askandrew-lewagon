from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from askandrew.api.chatbot import chatbot
from askandrew.ml_logic.question_answer import user_input  # Adjust this import based on your file structure

from askandrew.ml_logic.init_setup import database_loading
from askandrew.ml_logic.llm_setup import start_llm
from askandrew.ml_logic.question_answer import user_input, answer_ss, answer_mmr, llm_based_answer
from askandrew.api.api import *

from langchain_openai import OpenAIEmbeddings
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, message="The function `__call__` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#class Query(BaseModel):
#    question: str
#    user: Optional[str] = None

@app.get("/chat")
def chat(question):

    vectordb = database_loading() #returns vectordb
    qa_chain_mr = start_llm(vectordb)
    #   question = user_input()
    output = answer_mmr(vectordb, question)
    response = llm_based_answer(output, qa_chain_mr, question)

#    Process the input question through user_input function before sending to chatbot
#    processed_question = user_input(query.question)

    # Now call your chatbot's processing function with the processed question
#    response = chatbot(response)

    return {"question": question, "response": response}




'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from chatbot import llm_based_answer, user_input  # Assuming your chatbot logic is in chatbot.py

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/chat/")
def chat(question: Question):
    try:
        # You might need to adjust this part based on how llm_based_answer works and returns data
        answer = llm_based_answer(question.question)  # Make sure llm_based_answer can handle string directly
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
'''
