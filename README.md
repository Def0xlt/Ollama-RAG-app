# 🚀 Local RAG API to Kubernetes: End-to-End DevOps Pipeline

This project is a fully local Retrieval-Augmented Generation (RAG) API built to bridge the gap between application development and scalable infrastructure. It uses a local Large Language Model (LLM) to ensure data privacy and efficiency, combining vector search with dynamic context retrieval to generate grounded, accurate responses. 

What started as a local FastAPI application has been containerized with Docker, orchestrated via a self-healing Kubernetes cluster, and fully automated using a GitHub Actions CI/CD pipeline with strict semantic quality control.

---

## 🚀 Features

* **100% Local Processing:** No external API keys required. All embeddings and inferences run locally to ensure complete data privacy.
* **Dynamic Data Ingestion:** Easily feed new documents and context into the vector database on the fly via the `/add` endpoint or by dropping `.txt` files into the `docs/` folder.
* **Context-Aware Querying:** The `/query` endpoint retrieves the most relevant document chunks and uses them to ground the LLM's responses.
* **Portable Containerization:** Packaged into a lightweight Docker image for consistent deployment across any environment.
* **Self-Healing Infrastructure:** Deployed on Kubernetes (Minikube) to ensure high availability, resource management, and automatic pod restarts.
* **Automated Quality Control:** A GitHub Actions CI/CD pipeline runs deterministic semantic regression tests on every push using a custom "Mock LLM Mode."

## 🛠️ Tech Stack

* **Application Logic:** Python, FastAPI
* **Vector Database:** ChromaDB
* **Local LLM Runner:** Ollama (TinyLlama model)
* **Containerization:** Docker, Docker Hub
* **Orchestration:** Kubernetes (Minikube)
* **Automation & CI/CD:** GitHub Actions, Git

---

## 🗺️ System Architecture

**1. Overall RAG Data Flow**
<img src="./imgs/rag.png" alt="RAG Architecture Diagram" width="800">
*Shows the data ingestion from documents to ChromaDB, and the query routing from FastAPI to the local Ollama instance.*

**2. Kubernetes Orchestration Flow**
<img src="./imgs/kubernetes.png" alt="Kubernetes Flow Diagram" width="800">
*Illustrates the traffic flow from NodePort → Service Port → Target Port, and the Deployment managing the self-healing Pods.*

**3. CI/CD & GitOps Pipeline**
<img src="./imgs/gitops.jpeg" alt="GitOps Pipeline Diagram" width="800">
*Maps the GitHub Actions trigger on push, the semantic testing phase, and the deployment rollout strategy.*

---

## 📁 Project Structure

* `app.py`: The main FastAPI application containing the API endpoints and the Mock LLM testing logic.
* `embed_docs.py`: Utility script that automatically iterates through the `docs/` directory to generate embeddings and ingest them into ChromaDB.
* `docs/`: Directory containing all knowledge base `.txt` files.
* `semantic_test.py`: QA script that verifies the retrieval accuracy and data quality of the RAG responses.
* `Dockerfile`: Multi-stage build instructions for packaging the API.
* `.github/workflows/ci.yml`: The GitHub Actions pipeline configuration.
* `deployment.yaml` & `service.yaml`: Declarative Kubernetes manifests for cluster orchestration.

---

## ⚙️ Prerequisites & Quick Start

Before you begin, ensure you have Python 3.11+ and [Ollama](https://ollama.com/) installed and running on your host machine.

1. **Pull the TinyLlama model:**
   ```bash
   ollama pull tinyllama
   ```

2. **Install local dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API Locally:**
   ```bash
   uvicorn app:app --reload
   ```

### 🐳 Run via Docker

```bash
docker pull <your-dockerhub-username>/rag-app:latest
docker run -p 8000:8000 --add-host=host.docker.internal:host-gateway rag-app
```

### ☸️ Deploy to Kubernetes

```bash
minikube start
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service rag-app-service --url
```

---

## 📖 DevOps Engineering Journey & Documentation

### Why I Built This
I engineered this project to bridge the gap between application development and scalable infrastructure by successfully integrating AI deployments with strict quality control. I wanted to brush up on my core DevOps concepts and master how production systems handle automated testing at scale. A major takeaway from this build is the importance of semantic testing and treating deployment pipelines as code (IaC) to eliminate manual configuration drift and ensure reliable AI outputs.

### Phase 1: Local API & RAG Integration
I built the core RAG API to retrieve information by converting queries into vector embeddings and searching the local ChromaDB for semantic matches before passing the context to the LLM. I verified the internal networking between FastAPI, ChromaDB, and the local Ollama service by successfully generating accurate answers via `POST` requests to the `/query` endpoint.

### Phase 2: Docker Containerization
To solve the "it works on my machine" problem, I packaged the application into a Docker image. I utilized bridge networking (`host.docker.internal`) to allow the lightweight containerized API to communicate seamlessly with the heavy Ollama service running directly on the host machine, optimizing image size and resource allocation.

### Phase 3: Kubernetes Orchestration
I transitioned from managing single containers to declarative infrastructure using Minikube. By authoring `deployment.yaml` and `service.yaml` manifests, I deployed the application into a self-healing cluster. This setup guarantees high availability; if a pod crashes, the Kubernetes control plane automatically spins up a replacement to maintain the desired state, while the NodePort service ensures stable network routing.

### Phase 4: CI/CD, Semantic Testing & Mock LLM Mode
To prevent degraded knowledge base updates from reaching production, I created semantic tests that validate data quality rather than just code logic. Because LLMs generate non-deterministic text, I engineered a **Mock LLM Mode** triggered by the `USE_MOCK_LLM=1` environment variable. This bypasses the generation phase, allowing the GitHub Actions CI pipeline to deterministically validate the vector database's retrieval logic instantly on every push.

### Phase 5: Scaling with Multiple Documents
I refactored the system to use a `docs/` folder structure, creating an `embed_docs.py` script that automatically processes all text files in the directory. The CI pipeline successfully validated the expanded knowledge base, immediately catching data quality issues (missing keywords) when new files were introduced, proving the pipeline's ability to safely scale the application.