from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import joblib
import os

app = FastAPI()
router = APIRouter(prefix="/v1")


class Message(BaseModel):
    model: str
    version: float
    message: str


@router.post("/predict")
async def predict(data: Message):

    path = [os.path.dirname(__file__), 'bin', f'{data.model}-{data.version}.joblib']
    model = joblib.load(os.path.join(*path))
    
    vector = model.named_steps.vectorizer.transform([data.message])
    result = model.named_steps.model.predict(vector)

    return {
        "message": data.message,
        "model": data.model,
        "version": data.version,
        "result": result[0],
    }

app.include_router(router)
