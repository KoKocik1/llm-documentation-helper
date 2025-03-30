from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def ingest_docs():
    loader = ReadTheDocsLoader(
        path="langchain-docs/api.python.langchain.com/en/latest/"
    )
    raw_documents = loader.load()
    print(f"Found {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    chunks = text_splitter.split_documents(raw_documents)
    print(f"Split into {len(chunks)} chunks")

    for chunk in chunks:
        new_url = chunk.metadata["source"]
        new_url = new_url.replace("langchain-docs", "https:/")
        chunk.metadata.update({"source": new_url})

    PineconeVectorStore.from_documents(
        chunks,
        embeddings,
        index_name=os.getenv("PINECONE_INDEX_NAME"),
    )
    print("Documents ingested successfully")


if __name__ == "__main__":
    ingest_docs()
