from fastapi import FastAPI, Request
from pydantic import BaseModel
from final_code.supervisor.top_level import supervisor

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    response = supervisor.invoke({"question": request.question})
    return {"answer": response.get("final_output", "No answer generated.")}
