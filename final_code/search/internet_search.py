from langchain.tools import TavilySearchResults

def internet_search(state: dict):
    tavily_search = TavilySearchResults(max_results=3)
    search_docs = tavily_search.invoke(state["question"])
    formatted = "\n\n---\n\n".join(
        [f'<Document href="{doc["url"]}">\n{doc["content"]}\n</Document>' for doc in search_docs]
    )
    return {"context": [formatted]}
