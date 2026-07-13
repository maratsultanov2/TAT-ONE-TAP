from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tat import TAT

app = FastAPI(title="TAT-ONE-TAP API", version="1.0")
tat = TAT(mode='defense')

class DataInput(BaseModel):
    data: list
    window: int = 10
    block_sizes: list = None

@app.post("/detect_anomalies")
async def detect_anomalies(input_data: DataInput):
    try:
        preds = tat.detect_anomaly(
            input_data.data,
            window=input_data.window,
            block_sizes=input_data.block_sizes
        )
        return {"anomalies": preds.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok", "mode": tat.mode}
