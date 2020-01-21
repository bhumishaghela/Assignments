import requests,json
url="https://api.ipgeolocation.io/astronomy?apiKey=21df03644598450abf854676f192cb27&date=2020-01-21"
json_url=requests.get(url)
print(json_url.status_code)
print(json_url.text)


#http://stellarium-web.org/api/objects/find?str=moon
