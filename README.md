
# NQ Order Flow AI — MVP

This project is a starter architecture for a NASDAQ order-flow intelligence system.

## Features
- Live order book ingestion
- Buy vs seller dominance engine
- Delta calculations
- Large order detection
- Liquidity imbalance detection
- REST API backend
- React frontend dashboard

## Suggested Data Providers
- DataBento
- Rithmic
- dxFeed
- Interactive Brokers
- NASDAQ TotalView

## Backend Stack
- Python
- FastAPI
- WebSockets
- Pandas
- NumPy

## Frontend Stack
- React
- Next.js
- Lightweight Charts

## Run Backend

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Run Frontend

```bash
npm install
npm run dev
```

## Future Features
- Heatmap
- Iceberg detection
- Spoofing detection
- AI commentary
- Institutional flow scoring
