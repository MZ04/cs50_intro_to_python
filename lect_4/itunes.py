import json
import requests
import sys

if len(sys.argv) != 3:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit="+sys.argv[2]+"&term=" + sys.argv[1])
#Request.get(<URL>) returns a JSON related to the URL inserted
#print(json.dumps(response.json(), indent=2))
#For a right indentation we can use json.dumps
o = response.json()
for result in o["results"]: #there can be more than a result 
    print(result["trackName"]) #for each result we print the corrispondent track name = key in the dictionary "result"