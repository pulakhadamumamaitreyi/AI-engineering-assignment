from fastapi import FastAPI, WebSocket
from agent import agent_response
from language import detect_language
from memory import save_session, get_session
import uuid
import time

app = FastAPI()

@app.websocket("/chat")

async def chat(ws: WebSocket):

    await ws.accept()

    session_id = str(uuid.uuid4())

    while True:

        message = await ws.receive_text()

        start = time.time()

        language = detect_language(message)

        response = agent_response(message)

        save_session(session_id, {
            "last_message": message,
            "language": language
        })

        latency = (time.time() - start) * 1000

        await ws.send_json({
            "response": response,
            "language": language,
            "latency_ms": latency
        })
