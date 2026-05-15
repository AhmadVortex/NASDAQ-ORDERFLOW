
from fastapi import FastAPI
from engine import analyze_orderflow

app = FastAPI()

sample_orderbook = {
    "bids": [
        {"price": 21250, "size": 120},
        {"price": 21249, "size": 300},
        {"price": 21248, "size": 450},
    ],
    "asks": [
        {"price": 21251, "size": 600},
        {"price": 21252, "size": 400},
        {"price": 21253, "size": 150},
    ]
}

@app.get("/")
def root():
    return {"message": "NQ Order Flow AI running"}

@app.get("/analysis")
def analysis():
    return analyze_orderflow(sample_orderbook)
