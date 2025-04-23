from langchain.document_loaders import UnstructuredURLLoader
from final_code.utils.vector_store import create_vector_store
from final_code.config import urls

def url_search(query: dict):
    doc_loader = UnstructuredURLLoader(urls=urls)
    docs = doc_loader.load()
    vector_store = create_vector_store(docs, "python_docs")
    results = vector_store.as_retriever().invoke(query["question"])
    return {"Document_Search3_Results": "\n".join([doc.page_content for doc in results])}
