from publish.reviewer import review_content
from publish.writer import writer
from langchain.agents import create_react_agent, create_supervisor
from final_code.config import llm

reviewing_agent = create_react_agent(llm, [review_content], name="reviewing_agent", prompt="You are a reviewing expert.")
writing_agent = create_react_agent(llm, [writer], name="writing_agent", prompt="You write the final content.")

publishing_team = create_supervisor(
    [reviewing_agent, writing_agent],
    model=llm,
    prompt=(
        "Manage a reviewing and a writing agent.\n"
        "Use `reviewing_agent` for corrections.\n"
        "Use `writing_agent` to generate the final output."
    )
).compile(name="publishing_team")
