# Local RAG API with FastAPI & Ollama

This project is a fully local Retrieval-Augmented Generation (RAG) API built to bridge the gap between DevOps workflows and modern AI integrations. It uses a local Large Language Model (LLM) to ensure data privacy and efficiency, combining vector search with dynamic context retrieval to generate grounded, accurate responses.

## 🚀 Features

* **100% Local Processing:** No external API keys required. All embeddings and inferences run locally.
* **Dynamic Data Ingestion:** Easily feed new documents and context into the vector database on the fly via the `/add` endpoint.
* **Context-Aware Querying:** The `/query` endpoint retrieves the most relevant document chunks and uses them to ground the LLM's responses.
* **Fast & Modern:** Built on FastAPI for high performance and automatic interactive API documentation.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** FastAPI
* **Vector Database:** ChromaDB
* **Local LLM Runner:** Ollama
* **Model:** TinyLlama

## 📁 Project Structure

* `app.py`: The main FastAPI application containing the `/add` and `/query` endpoints.
* `embed.py`: A utility script for generating initial embeddings and managing document chunking and ingestion into ChromaDB.

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
1. Python 3.11+
2. [Ollama](https://ollama.com/) installed and running on your machine.

Once Ollama is installed, pull the TinyLlama model:

```bash
ollama pull tinyllama