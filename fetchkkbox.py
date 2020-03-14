import json
import requests

CLIENT_ID = "xxx"
CLIENT_SECRET = "xxx"

def get_token():
    r = requests.post("https://account.kkbox.com/oauth2/token", data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        })
    return r.json()


def search(token, q):
    s = requests.get("https://api.kkbox.com/v1.1/search?territory=TW&type=track&limit=1&q=" + q, headers={
            "Authorization": token['token_type']+' '+token['access_token']
        })
    tracks = s.json()
    songs = tracks['tracks']['data']
    if len(songs) > 0:
        return songs[0]
    return None

def track_data(token, id):
    s = requests.get(f"https://api.kkbox.com/v1.1/tracks/{id}?territory=TW", headers={
            "Authorization": token['token_type']+' '+token['access_token']
        })
    return s.json()

def main():
    songs = []
    with open(input("songs.json: "), "r") as f:
        songs = json.load(f)
    
    counter = 0
    for song in songs:
        token = get_token()
        result = search(token, song["singer"]+" "+song["name"])
        if result:
            song["image"] = result["album"]["images"][-1]["url"]
        else:
            print(song["singer"] + " " + song["name"] + "not found")
            song["image"] = ""
        if counter % 1000 == 0:
            print(counter)
        counter += 1
    
    with open(input("output: "), "w") as f:
        json.dump(songs, f)

if __name__ == '__main__':
    main()
