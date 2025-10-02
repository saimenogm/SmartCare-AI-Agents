import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from chains.support_chain import handle_message


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/chat')
async def chat_endpoint(req: Request):
    body = await req.json()
    message = body.get('message')
    user_id = body.get('user_id')
    if not message:
        return {'error': 'message required'}
    raw = handle_message(message, user_id)   # whatever you already have

    # ensure the UI contract
    return {
        "response": raw.get("answer", str(raw)),   # fallback to whole object
        "intent": raw.get("intent", "general"),
        "sentiment": raw.get("sentiment", "neutral"),
        "escalated": raw.get("escalated", False),
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))