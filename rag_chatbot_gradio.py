from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import ConversationalRetrievalChain, RetrievalQA
from langchain_ollama import OllamaLLM
import os
from dotenv import load_dotenv
import gradio as gr

# llm


def llm():
    load_dotenv()
    API_KEY = os.getenv("OLLAMA_API_KEY")

    llm = OllamaLLM(
        model="gpt-oss:20b",
        base_url="https://ollama.com",
        client_kwargs={"headers": {"Authorization": f"Bearer {API_KEY}"}},
    )
    return llm


# File Loader
def file_loader(file):
    text_file = PyPDFLoader(file)
    doc = text_file.load()
    return doc


def text_splitter(document):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        separators=["\n\n", "\n", " ", ""],
        length_function=len,
    )
    chunk = splitter.split_documents(document)
    return chunk


def vector_store(chunk):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_db = Chroma.from_documents(chunk, embedding_model)
    return vector_db


# Retrieval Pipeline


def retriever(file):
    doc = file_loader(file)
    chunk = text_splitter(doc)
    vector_db = vector_store(chunk)
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    return retriever


def chatbot(file, query):
    coversation_chain = RetrievalQA.from_chain_type(
        llm=llm(),
        retriever=retriever(file),
        chain_type="stuff",
    )

    response = coversation_chain.invoke({"query": query})
    return response["result"]


demo = gr.Interface(
    fn=chatbot,
    inputs=[gr.File(label="Upload a file"), gr.Textbox(label="Ask any question")],
    outputs=[gr.Textbox(label="Answer")],
)
if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=True)
