from langchain.document_loaders import PyPDFLoader
from final_code.utils.vector_store import create_vector_store

def rag_search(query: dict):
    doc_loader = PyPDFLoader("Transformers for Machine Le_ (Z-Library).pdf")
    docs = doc_loader.load()
    vector_store = create_vector_store(docs, "rag_pdf_docs")
    results = vector_store.as_retriever().invoke(query.get("question", ""))
    return {"rag_search_results": "\n".join([doc.page_content for doc in results])}
