from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import openai
from openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Carregar modelo RAG (exemplo com BART)
'''
tokenizer_rag = AutoTokenizer.from_pretrained("facebook/rag-sequence-nq")
model_rag = AutoModelForSeq2SeqLM.from_pretrained("facebook/rag-sequence-nq")

def generate_response_llm(query):
    inputs = tokenizer_rag(query, return_tensors="pt")
    generated_ids = model_rag.generate(**inputs)
    response = tokenizer_rag.decode(generated_ids[0], skip_special_tokens=True)
    return response
'''

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_response_openai(query):
    llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )

    resposta = llm.invoke(f"Faça uma resposta baseada nessa resposta original, seja gentil: {query}")
    print(resposta.content)

    return resposta.content