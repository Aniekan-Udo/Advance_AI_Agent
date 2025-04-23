from final_code.search.rag_search import rag_search
from final_code.search.internet_search import internet_search
from final_code.search.url_search import url_search
from langchain.agents import create_react_agent, create_supervisor
from final_code.config import llm

rag_agent = create_react_agent(llm, [rag_search], name="rag_agent", prompt="You are a RAG tool with access to a file")
research_agent = create_react_agent(llm, [internet_search], name="research_agent", prompt="You are an expert Researcher")
url_agent = create_react_agent(llm, [url_search], name="url_agent", prompt="You are an expert researcher with access to URL links")

search_team = create_supervisor(
    [research_agent, rag_agent, url_agent],
    model=llm,
    prompt=(
        "You are a team supervisor managing a web search expert, a PDF search expert, and a URL search expert.\n"
        "- Use `research_agent` for current events or general knowledge.\n"
        "- Use `rag_agent` for PDF topics on ML transformers.\n"
        "- Use `url_agent` for Python basics and URLs."
    )
).compile(name="search_team")
