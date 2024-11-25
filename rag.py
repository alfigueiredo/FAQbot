from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Carregar modelo RAG (exemplo com BART)
tokenizer_rag = AutoTokenizer.from_pretrained("facebook/rag-sequence-nq")
model_rag = AutoModelForSeq2SeqLM.from_pretrained("facebook/rag-sequence-nq")

def generate_response(query):
    inputs = tokenizer_rag(query, return_tensors="pt")
    generated_ids = model_rag.generate(**inputs)
    response = tokenizer_rag.decode(generated_ids[0], skip_special_tokens=True)
    return response
