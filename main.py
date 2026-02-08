from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str
    mode: str

@app.post("/search")
def search(q: Query):
    # MOCK DATA (replace with scraping later)
    if q.mode == "quick":
        return {
            "results": [
                {
                    "name": q.query,
                    "platform": "Amazon Now",
                    "price": "99",
                    "link": "amazon://search"
                },
                {
                    "name": q.query,
                    "platform": "Flipkart Minutes",
                    "price": "95",
                    "link": "flipkart://search"
                }
            ]
        }
    else:
        return {
            "results": [
                {
                    "name": q.query,
                    "platform": "Amazon",
                    "price": "120",
                    "link": "amazon://search"
                },
                {
                    "name": q.query,
                    "platform": "Flipkart",
                    "price": "115",
                    "link": "flipkart://search"
                }
            ]
        }
