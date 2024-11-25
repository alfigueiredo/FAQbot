# Python RAGnarok! 
## Chatbot de FAQ usando com RAG e Bot no Telegram

Bem-vindo ao projeto **Python RAGnarok! Chatbot de FAQ usando com RAG e Bot no Telegram**! Este projeto demonstra como criar um chatbot inteligente para uma loja de livros utilizando **Retrieval-Augmented Generation (RAG)** e **Telegram**, empregando modelos de linguagem open source em português.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Criação e Armazenamento de Embeddings](#criação-e-armazenamento-de-embeddings)
- [Configuração e Execução do Bot do Telegram](#configuração-e-execução-do-bot-do-telegram)
- [Resolução de Problemas](#resolução-de-problemas)
- [Contribuições](#contribuições)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

Este projeto tem como objetivo criar um chatbot que responde perguntas frequentes (FAQ) sobre a loja de livros "Let's Read". Utilizamos a técnica de **Retrieval-Augmented Generation (RAG)** para combinar a recuperação de informações relevantes com a geração de respostas utilizando **Modelos de Linguagem Natural (LLMs)** open source em português. O chatbot está integrado ao Telegram, permitindo uma interação eficiente e personalizada com os usuários.

## Funcionalidades

- **Resposta a FAQs:** Responde a perguntas frequentes sobre produtos, pedidos, pagamentos, envio, devoluções, entre outros.
- **Integração com Telegram:** Permite que os usuários interajam com o chatbot diretamente pelo aplicativo Telegram.
- **Uso de RAG:** Combina recuperação de informações e geração de texto para fornecer respostas precisas e contextualizadas.
- **Embeddings com ChromaDB:** Armazena e consulta embeddings de forma eficiente para melhorar a precisão das respostas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Transformers (Hugging Face)**: Biblioteca para modelos de linguagem.
- **ChromaDB**: Banco de dados para armazenamento e consulta de embeddings.
- **Telegram Bot API**: Integração do chatbot com Telegram.
- **Torch**: Backend para modelos de linguagem.
- **Ollama**: Ferramenta para otimização na geração de embeddings (se aplicável).*

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados:

- **Python 3.7+**
- **pip**: Gerenciador de pacotes Python
- **Conta no Telegram**: Para criar e testar o bot
- **Token do Bot do Telegram**: Obtido através do [@BotFather](https://telegram.me/BotFather)

## Estrutura do Projeto

```
lets_read_chatbot/
│
├── data/faq.json
├── requirements.txt
├── create_embeddings.py
├── telegram_bot.py
└── README.md
```

- **faq.json**: Arquivo contendo as perguntas e respostas frequentes.
- **requirements.txt**: Lista de dependências do projeto.
- **create_embeddings.py**: Script para gerar e armazenar embeddings no ChromaDB.
- **telegram_bot.py**: Script para configurar e executar o bot no Telegram.
- **README.md**: Este arquivo de documentação.

## Configuração do Ambiente

### 1. Clone o Repositório

Primeiro, clone este repositório para sua máquina local:

```bash
git clone https://https://github.com/letsdata/oficina-rag-python-cerrado.git
cd oficina-rag-python-cerrado
```

### 2. Crie e Ative um Ambiente Virtual

É recomendado utilizar um ambiente virtual para gerenciar as dependências do projeto.

```bash
python -m venv rag_env
```

- **No Windows:**

  ```bash
  rag_env\Scripts\activate
  ```

- **No macOS/Linux:**

  ```bash
  source rag_env/bin/activate
  ```

### 3. Instale as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Verifique o Arquivo `data/faq.json`

Certifique-se de que o arquivo `faq.json` está presente na pasta 'data' do projeto e contém todas as perguntas e respostas necessárias. Você pode utilizar o conjunto de FAQs fornecido anteriormente ou personalizá-lo conforme suas necessidades.


### 1. Obtenha o Token do Bot do Telegram

- Abra o Telegram e inicie uma conversa com [@BotFather](https://telegram.me/BotFather).
- Use o comando `/newbot` e siga as instruções para criar um novo bot.
- Após a criação, você receberá um **Token de API**. Guarde-o, pois será necessário para configurar o bot.

### 2. Configure o Script `telegram_bot.py`

Abra o arquivo `telegram_bot.py` e substitua `"YOUR_TELEGRAM_BOT_TOKEN"` pelo token obtido do BotFather. (ou use um .env)

### 3. Execute o Bot

Com o ambiente virtual ativado e as dependências instaladas, execute o script do bot:

```bash
python telegram_bot.py
```

Você verá a mensagem:

```
Bot iniciado. Pressione Ctrl+C para parar.
```

Agora, seu bot está ativo e pronto para responder às mensagens no Telegram!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Se você tiver qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- **E-mail:** leonsolon@gmail.com
- **Site** https://letsdata.ai
- **LinkedIn:** [Seu Perfil](https://www.linkedin.com/in/leonsolon)

---

**Agradecimentos** por utilizar este projeto! Esperamos que ele seja útil para a criação do seu chatbot de FAQ. Se tiver alguma dúvida ou precisar de mais assistência, não hesite em entrar em contato.