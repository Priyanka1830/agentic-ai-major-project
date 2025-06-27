from crewai import Agent

class SerperSearchAgent(Agent):
    def __init__(self, ):
        pass

    def fetch_listings(self, query):
        serper_tool = NewSearchTool
        serp_results = serper_tool.search(query)
        return serp_results  # contains organic results, snippets, etc.


import http.client
import json

class NewSearchTool():
    def __init__(self, api_key=None):
        self.api_key = api_key

    def search(self, query, num_results=10):


        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
            "q": query,
            "num": num_results,
            "gl": "in"
        })
        headers = {
            'X-API-KEY': 'f0f3b3228c59f57eb2006047d65e8bdf094915f6',
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()
        data = res.read()
        result = data.decode("utf-8")
        return result