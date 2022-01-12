import json
import requests

def addSite(nickname, url):
  try:
    collection_slug = url.split('/')[4]
    apiUrl = "https://api.opensea.io/api/v1/collection/" + collection_slug
    response = requests.request("GET", apiUrl)
    info = json.loads(response.text)['collection']['primary_asset_contracts'][0]
    name = info['name']
    try:
      logo = info['image_url']
    except:
      logo = ""
      
    temp = {
      'name': name,
      'url': url,
      'apiUrl': apiUrl + "/stats",
      'logo': logo
    }
    
    with open('opensea.json', 'r') as f:
      site = json.load(f)
    
    site[nickname] = temp

    with open('opensea.json', 'w') as outfile:
      json.dump(site, outfile, indent=4)
      
    return True
  except:
    return False