from apiclient.discovery import build
import json

DEVELOPER_KEY = "your api key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

items = []


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == "__main__":
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    for ids in chunks([item['snippet']['resourceId']['videoId'] for item in json.load(open('items.json', 'r'))], 50):
        videos_response = youtube.videos().list(
            part="statistics",
            id=','.join(ids)
        ).execute()

        # print(videos_response)
        for item in videos_response.get("items", []):
            items.append(item)

    with open('videos.json', 'w') as outfile:
        json.dump(items, outfile)
