import os
from dotenv import load_dotenv
from langchain.document_loaders import PyMuPDFLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import chromadb


# load environment variables
load_dotenv()


def get_documents(doc_dir: str):
    loader = PyMuPDFLoader(doc_dir)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_documents(docs)


def create_chromadb_settings(db_dir: str):
    return chromadb.config.Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=db_dir,
        anonymized_telemetry=False
    )


def init_chromadb(db_dir: str, file_path: str):
    settings = create_chromadb_settings(db_dir)
    embeddings = OpenAIEmbeddings()

    vectorstore = Chroma(
        collection_name="langchain_store",
        embedding_function=embeddings,
        client_settings=settings,
        persist_directory=db_dir,
    )

    vectorstore.add_documents(documents=get_documents(file_path), embedding=embeddings)
    vectorstore.persist()


def query_chromadb(db_dir: str, query: str, k=3):
    settings = create_chromadb_settings(db_dir)
    embeddings = OpenAIEmbeddings()

    vectorstore = Chroma(
        collection_name="langchain_store",
        embedding_function=embeddings,
        client_settings=settings,
        persist_directory=db_dir,
    )

    docs = vectorstore.similarity_search_with_score(query=query, k=k)

    return [doc[0] for doc in docs]
