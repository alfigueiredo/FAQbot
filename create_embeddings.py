# create_embeddings.py

import json
from transformers import AutoTokenizer, AutoModel
import torch
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
print(chromadb.__version__)

import os
print(os.getcwd())

# Carregar FAQ
with open('data/faq.json', 'r', encoding='utf-8') as f:
    faq = json.load(f)

# Configurar tokenizer e modelo
tokenizer = AutoTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
model = AutoModel.from_pretrained("neuralmind/bert-base-portuguese-cased")

# Função para obter embeddings
# Esta função recebe um texto, tokeniza-o e passa pelo modelo BERT para obter os embeddings.
# Os embeddings são a média dos estados ocultos da última camada do modelo.
def get_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# Configurar ChromaDB
# Especifique o diretório de persistência
persist_directory = "./chroma_storage"

# Se a pasta de persistência não existir, crie-a
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

# Inicializar o cliente ChromaDB
client = chromadb.Client(Settings(is_persistent=True, persist_directory=persist_directory))

# Verificar se a coleção já existe
lista_colecoes = [collection.name for collection in client.list_collections()]
if "faq_collection" not in lista_colecoes:
    collection = client.create_collection("faq_collection")
    
    # Adicionar FAQs à coleção
    for idx, item in enumerate(faq):
        embedding = get_embeddings(item['pergunta'])
        collection.add(
            documents=[item['pergunta']],
            metadatas=[{"resposta": item['resposta']}],
            embeddings=[embedding],
            ids=[str(idx)]
        )

print("Embeddings criados e armazenados com sucesso!")
