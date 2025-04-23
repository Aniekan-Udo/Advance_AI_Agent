from final_code.supervisor.search_team import search_team
from final_code.supervisor.search_team import publishing_team
from langchain.agents import create_supervisor
from final_code.config import llm

supervisor = create_supervisor(
    [search_team, publishing_team],
    model=llm,
    prompt=(
        "You manage two teams: `search_team` and `publishing_team`.\n"
        "1. Delegate query to `search_team`.\n"
        "2. Pass result to `publishing_team`.\n"
        "3. Return final result only — no intermediate steps."
    ),
    output_mode="full_history"
).compile(name="top_level_supervisor")
