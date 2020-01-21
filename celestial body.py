
import requests,json
url = "http://stellarium-web.org/api/objects/find?str=sun"
json_url=requests.get(url)
print(json_url.text)
data = json.loads(json_url.text)
print(data.text)
