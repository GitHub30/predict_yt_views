from apiclient.discovery import build
import json

DEVELOPER_KEY = "your api key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

playlistId = "UURxDTCmIjgli-Xgh2KPE9dA"
items = []


def youtube_saerch_video(next_page_token = ""):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    videos_response = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlistId,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    # print(videos_response)
    for item in videos_response.get("items", []):
        items.append(item)
    # return
    if 'nextPageToken' in videos_response:
        youtube_saerch_video(videos_response["nextPageToken"])


if __name__ == "__main__":
    youtube_saerch_video()
    with open('items.json', 'w') as outfile:
        json.dump(items, outfile)
