from askandrew.ml_logic.init_setup import database_loading
from askandrew.ml_logic.llm_setup import return_llm, start_llm
from askandrew.ml_logic.question_answer import user_input, answer_mmr, llm_based_answer

def main():
    # Call the user_input function to get the question from the user.
    question = user_input()

    # Call the llm_based_answer function, passing the question, to generate and print the answer.
    llm_based_answer(question)

if __name__ == "__main__":
    main()
