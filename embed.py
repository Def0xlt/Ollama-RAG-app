import chromadb
import os

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("docs")


# clear any collections that exist inside the docs/ folder

existing_ids = collection.get()["ids"]
if existing_ids:
    collection.delete(ids=existing_ids)

for filename in os.listdir("docs/"):
    if filename.endswith(".txt"):
        with open(f"docs/{filename}", "r") as f:
            text = f.read()
        collection.add(documents=[text], ids=[filename])

print("Re-embedded all documents in chroma db successfully")
    
# with open("k8s.txt", "r") as f:
#     text = f.read()

# collection.add(documents=[text], ids=["k8s"])

# print("embedding added to chroma db successfully")