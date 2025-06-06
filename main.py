from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.router_chat import router as chat_router
from routers.router_model import router as model_router

app = FastAPI(
    title="Chatbot API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router)
app.include_router(model_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
