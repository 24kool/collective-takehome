from fastapi import FastAPI
import uvicorn
from utils import stream_csv_as_dict

app = FastAPI(
    title="Collective: Take-home by KC Kim",
    version="1.0.0",
)

@app.get("/validate")
def validate():
    # Stream and convert to list to see the data
    bank_balances = list(stream_csv_as_dict("data/bank_balances.csv"))
    transactions = list(stream_csv_as_dict("data/transactions.csv"))
    
    print("Bank Balances:")
    for row in bank_balances:
        print(row)
    
    print("\nTransactions:")
    for row in transactions:
        print(row)
    
    res = []
    return {"results": res}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)