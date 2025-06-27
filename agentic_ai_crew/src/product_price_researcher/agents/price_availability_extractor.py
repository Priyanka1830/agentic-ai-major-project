import re
from crewai import Agent

class PriceAvailabilityExtractor(Agent):
    def extract(self, serp_results):
        competitors = []
        for res in serp_results.get("organic", []):
            title = res.get("title", "")
            snippet = res.get("snippet", "")
            link = res.get("link", "")

            # Simple regex to pull "$123.45"-like price
            price_match = re.search(r'\\$\\d{1,6}(\\.\\d{2})?', title + " " + snippet)
            price = price_match.group(0) if price_match else None
            stock = "out of stock" not in (title + snippet).lower()

            # Find competitor from domain (refine as needed)
            seller = link.split("/")[2] if "://" in link else link.split("/")[0]

            if price:
                competitors.append({
                    "seller": seller,
                    "price": price,
                    "in_stock": stock,
                    "link": link
                })
        return competitors
