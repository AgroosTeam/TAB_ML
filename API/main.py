from fastapi import FastAPI
from text_cleaner import TextCleaner
import pickle

app = FastAPI()

with open("ML/trained_model/model.pkl", "rb") as f:
    model, cv = pickle.load(f)


@app.post("/predict/{message}")
async def scoring_text(message: str):
    new_corpus = [TextCleaner.clear_text(message)]
    prediction = model.predict(cv.transform(new_corpus).toarray())
    return {"prediction": bool(prediction)}
