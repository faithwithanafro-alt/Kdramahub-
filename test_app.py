import requests

API_KEY = "96c3b15c58e34abde94f9fdbe5de9960" # my key on TMDB 
BASE_URL = "https://api.themoviedb.org/3"

def search_kdrama(query):
    url = f"{BASE_URL}/search/tv" #API door for code to questions about the drama typed in

    params = { #params keeps info in a box so it can be reuse so i dont have to rewrite stuff
        "api_key": API_KEY,
        "query": query,
        "language": "en-US",
        "with_origin_country": "KR"
        
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["results"]:
        drama = data["results"][0]
        print(f"Title: {drama['name']}")
        print(f"Overview: {drama['overview']}")
        print(f"Rating: {drama['vote_average']}/10")
    else:
        print("No drama found")

search_kdrama("True Beauty")