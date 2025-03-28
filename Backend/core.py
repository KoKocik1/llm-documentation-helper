from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from langchain.chains.retrieval import create_retrieval_chain
from dotenv import load_dotenv
import os

load_dotenv()

EMBEDDING_MODEL = "text-embedding-3-small"
LANGCHAIN_HUB = "langchain-ai/retrieval-qa-chat"


def run_llm(query):
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vectorstore = PineconeVectorStore(
        index_name=os.getenv("PINECONE_INDEX_NAME"),
        embedding=embeddings,
    )
    chat = ChatOpenAI(model="gpt-4o-mini", temperature=0, verbose=True)
    retriever = hub.pull(LANGCHAIN_HUB)

    stuff_documents_chain = create_stuff_documents_chain(
        chat,
        retriever
    )

    qa = create_retrieval_chain(
        retriever=vectorstore.as_retriever(),
        combine_docs_chain=stuff_documents_chain,
    )

    result = qa.invoke({"input": query})
    return result["answer"]


if __name__ == "__main__":
    result = run_llm("What is LangChain?")
    print(result)
