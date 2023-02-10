import requests

url = "https://viperscore.p.rapidapi.com/sports"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "viperscore.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)