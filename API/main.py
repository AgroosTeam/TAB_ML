from fastapi import FastAPI
from pydantic import BaseModel
from text_cleaner import TextCleaner
import pickle

app = FastAPI()

with open("ML/trained_model/model.pkl", "rb") as f:
    model, cv = pickle.load(f)


class ScoringItem(BaseModel):
    text: str


@app.post("/predict")
async def scoring_text(item: ScoringItem):
    new_corpus = [TextCleaner.clear_text(item.text)]
    prediction = model.predict(cv.transform(new_corpus).toarray())
    return {"prediction": bool(prediction)}
