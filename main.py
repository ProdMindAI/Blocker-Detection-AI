from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

app = FastAPI(title="ProdMind AI - PMBuddy Prototype")

# Should eventually be replaced with a more robust storage solution
INFO_PATH = "data/sample.txt"

class QueryRequest(BaseModel):
    question: str

@app.on_event("startup")
def load_documents():
    global retriever, qa_chain

    if not os.path.exists(INFO_PATH):
        with open(INFO_PATH, "w") as f:
            f.write("Placeholder content: product specs, roadmaps, release notes.")

    loader = TextLoader(INFO_PATH)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    retriever = vectorstore.as_retriever()

    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

@app.post("/ask")
def ask_pmbuddy(request: QueryRequest):
    try:
        result = qa_chain.run(request.question)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "PMBuddy Prototype is live. POST to /ask to interact."}
