from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

def initialize_llama():
    llm = Ollama(model="llama3")
    return llm

def summarize_text(llm, text: str) -> str:
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="Sumarize o seguinte texto: {text}"
    )

    llm_sequence = prompt_template | llm

    summary = llm_sequence.invoke({"text": text})
    return summary


