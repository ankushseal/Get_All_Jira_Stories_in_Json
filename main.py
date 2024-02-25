# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://testing500.atlassian.net/rest/api/3/issue/TES-2"

auth = HTTPBasicAuth("25092000ankushseal@gmail.com", "ATATT3xFfGF0JX-nib0WoBch7r7sCZ29xX8P0HqJXd4uuub3bTkpknpu9ggS90FPNwok0FJttq3s3KOdWY2NJM9yKr4ZiPuaqfoIMpMN3zug4pq3lsPDvHInrQiZ_77nSLXlWu7mIQbiT-TuGKnKkiBUbMu9_AURZPXOTHwKdFlMyvo-PU-cFMk=B7D377E7")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
