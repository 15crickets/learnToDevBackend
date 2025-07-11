from fastapi import FastAPI
import googleapiclient.discovery

api_service_name = "youtube"
api_version = "v3"

DEVELOPER_KEY = 

app = FastAPI()

@app.get("search/{query}")
async def search(query):




    return 0
