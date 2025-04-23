from langchain.vectorstores import Chroma
from final_code.config import embedding_model, text_splitter

def create_vector_store(docs, collection_name: str):
    chunks = text_splitter.split_documents(docs)
    return Chroma.from_documents(documents=chunks, collection_name=collection_name, embedding=embedding_model)
