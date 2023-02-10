import requests

url = "https://viperscore.p.rapidapi.com/sports"

headers = {
	"X-RapidAPI-Key": "71d411b83cmshb7b1cee17c5afa3p1c914ejsnde8d0527c7ad",
	"X-RapidAPI-Host": "viperscore.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)