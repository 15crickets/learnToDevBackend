from fastapi import FastAPI
import googleapiclient.discovery
from dotenv import load_dotenv
import os
import pprint as pprint

load_dotenv()

api_service_name = "youtube"
api_version = "v3"

DEVELOPER_KEY = os.getenv("GOOGLE_API_KEY")

app = FastAPI()

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY
)

async def videoSearch(videoIds):

    videos = []
    for item in videoIds: 
        request = youtube.videos().list(
            part="statistics",
            id=item
        )

        response = request.execute()
        videos.append(response)


    return videos

def scoreVideos (videos):
    videoScores = []

    for video in videos:
        if(video["likeCount"] > 0):
            videoScores.append(video["viewCount"]/video["likeCount"])

        else:
            videoScores.append(0)

    

    return videoScores


async def youtubeSearch(query):

    request = youtube.search().list(
        part="snippet",
        maxResults = 10,
        q=query,
        type="video",
        order="relevance"
    )

    response = request.execute()

    videoIds = []
    for item in response["items"]:
        videoIds.append(item["id"]["videoId"])


    print(videoIds)
    videos = await videoSearch(videoIds)
    scoreVideos(videos)

    return response


async def redditSearch(query):
    return 0



async def stackSearch(query):
    return 0



@app.get("/search/{query}")
async def search(query):
    print("Hi")

    youtubeResponse = await youtubeSearch(query)
    print(youtubeResponse)



    
    
    return 0


