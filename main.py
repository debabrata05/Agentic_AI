from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.graph import build_graph

app = FastAPI(title="Sovereign Agent API")

class Request(BaseModel):
    query: str

@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        # Build the graph (loads tools dynamically)
        agent = await build_graph()
        
        # Run the agent
        initial_state = {"messages": [("user", request.query)]}
        result = await agent.ainvoke(initial_state)
        
        # Extract last message
        last_msg = result["messages"][-1].content
        return {"response": last_msg}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Run: python main.py
    uvicorn.run(app, host="0.0.0.0", port=8000)
