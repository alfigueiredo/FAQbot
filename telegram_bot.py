# telegram_bot.py

import json
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import chromadb
from chromadb.config import Settings
import torch
from transformers import AutoTokenizer, AutoModel
import os
from dotenv import load_dotenv
from create_embeddings import get_embeddings
#from rag import generate_response_llm
from rag import generate_response_openai

# Configurar ChromaDB
# Especifique o diretório de persistência
persist_directory = "./chroma_storage"

# Se a pasta de persistência não existir, crie-a
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

# Inicializar o cliente ChromaDB
client = chromadb.Client(Settings(is_persistent=True, persist_directory=persist_directory))
collection = client.get_collection("faq_collection")

# Configurar tokenizer e modelo
tokenizer = AutoTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
model = AutoModel.from_pretrained("neuralmind/bert-base-portuguese-cased")

async def iniciar_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Inicializa o bot.

    Args:
        update (Update): Objeto Update do Telegram
        context (ContextTypes.DEFAULT_TYPE): Objeto Context do Telegram
    """
    await update.message.reply_text(
        "Olá! Eu sou o Bot do Let's Read! Bem-vindos à Python Cerrado + Plone Conference! O que deseja saber sobre nossa loja?"
    )


# Função para responder mensagens
async def tratar_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"Mensagem recebida: {user_message}")

    embedding_user_message = get_embeddings(user_message)

    # Recuperar resposta do ChromaDB
    results = collection.query(query_embeddings=[embedding_user_message], n_results=1)

    if results['metadatas'][0]:
        resposta = results['metadatas'][0][0]['resposta']
        similaridade = results['distances'][0][0]
        print(f"Similaridade: {similaridade}")
    else:
        resposta = "Desculpe, não encontrei uma resposta para sua pergunta."

    # Opcional: Gerar uma resposta adicional com RAG
    # resposta_rag = generate_response_llm(user_message)
    # resposta_final = f"{resposta}\n\n{resposta_rag}"
    
    #resposta_openai = generate_response_openai(user_message)

    # Para simplificar, vamos usar apenas a resposta do ChromaDB
    await update.message.reply_text(resposta)
    #await update.message.reply_text(resposta_openai)

def main():
    load_dotenv()
    application = Application.builder().token(os.getenv("TELEGRAM_API_TOKEN")).build()
    application.add_handler(CommandHandler("start", iniciar_bot))

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, tratar_mensagem)
    )

    application.run_polling()
    print("Bot aguardando mensagens!")

if __name__ == '__main__':
    main()
