# Anime Recommendation System — LLM + LLMOps

This repository implements a **scalable anime recommendation system** that combines **Large Language Models (LLMs)** with modern **AI engineering (LLMOps)** practices to deliver AI-enhanced recommendations, vector search, and an end-to-end pipeline for ingesting and querying anime metadata.

> The goal of this project is to build a secure, schema-aware, and production-oriented anime recommendation system that enables natural-language interactions and deployment-ready workflows.  
The system bridges semantic AI and structured data to support both developer workflows and user-facing recommendations.


---

## Features & Components

### 🔹 Application Layer 
- Interactive UI for recommendations
- Streamlit demo interface

### 🔹 LLM + Embeddings Backend
- Use of **vector embeddings** for semantic similarity search  
- ChromaDB for **fast ANN (Approximate Nearest Neighbor) search**
- LLMs (OpenAI, local options) for **contextual ranking** and explanations

### 🔹 LLMOps Workflows
- Orchestrated pipelines for:
  - Embedding generation
  - Vector store creation
  - Model inference
  - Reproducible experiment tracking

### 🔹 Deployment & Scaling
- Docker container for local testing  
- Kubernetes YAML manifests for cloud deployment  
- Designed for **scalable API endpoints**

  ##  System Workflow

1. **Data ingestion**: Anime metadata, synopsis, and features loaded  
2. **Vectorization**: Textual anime information → embeddings  
3. **Indexing**: Embeddings stored in ChromaDB for fast lookup  
4. **User query**: Natural language query from UI or API  
5. **Semantic retrieval**: Nearest neighbour search in vector index  
6. **LLM augmentation**: Optionally refine or rerank with LLM  
7. **Results delivered**: Recommendations returned with metadata

---

## Tech Stack

| Layer | Technologies |
|-------|--------------|
| UI / API | Streamlit |
| Embeddings | HuggingFace, OpenAI, ChromaDB |
| Backend | Python |
| Deployment | Docker, Kubernetes |
| Workflow | LLMOps pipelines |


The application layer currently uses Streamlit for interactive recommendations. The architecture allows future extension to REST APIs if required.

---

About the Anime Dataset

This system ingests anime metadata and description text to power embeddings and retrieval. Typical datasets in this domain include community-sourced collections with genre, rating, and synopsis fields (see similar examples of anime data sources used in open recommendation projects).


---

# Run Locally
- Start backend API
  
  python -m app.main

# Run Streamlit (if included)

  streamlit run app/app.py

# Run with Docker

  docker build -t anime-recomender.
 
  docker run -p 8501:8501 anime-recomender

# Kubernetes (LLMOps)
- The llmops-k8s.yaml includes manifests to deploy the system on a Kubernetes cluster:

   kubectl apply -f llmops-k8s.yaml
