from fastapi import FastAPI
import chromadb
import ollama

app = FastAPI()
chroma = chromadb.PersistentClient(path="./chroma_db")
collection = chroma.get_or_create_collection("docs")

@app.post("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama.generate(
        model="tinyllama",
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}


@app.post("/add")
def add_document(doc: str):
    import uuid
    doc_id = str(uuid.uuid4())
    collection.add(documents=[doc],ids=[doc_id])
    return {
        "request": doc,
        "message": "Document added successfully",
        "document_id": doc_id
    }
