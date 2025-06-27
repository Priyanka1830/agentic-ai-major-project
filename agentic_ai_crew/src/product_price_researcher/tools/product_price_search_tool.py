import requests

class SerperSearchTool:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "<https://serper.dev/api/search>"

    def search(self, query, num_results=10):
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "q": query,
            "num": num_results,
            "gl": "in"  # country code (optional)
        }
        response = requests.post(self.url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()  # returns dict with SERP info


import json
import os

from langchain.tools import tool

class SearchTools():

  @tool("Search internet")
  def search_internet(query):
    """Search the internet"""
    return SearchTools.search(query)

  def search(query, num_results=5):
    url = "https://google.serper.dev/search"
    payload = {
            "q": query,
            "num": num_results,
            "gl": "in"  # country code (optional)
        }
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    print("results:")
    print(results)

    stirng = []
    for result in results:
      try:
        stirng.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    content = '\n'.join(stirng)
    return f"\nSearch result: {content}\n"