import os
from tools import SerperSearchTool
from agents.product_query_generator import ProductQueryGenerator
from agents.serper_search_agent import SerperSearchAgent
from agents.price_availability_extractor import PriceAvailabilityExtractor
from agents.change_detector import ChangeDetector
from agents.pricing_advisor import PricingAdvisor
from dotenv import load_dotenv
load_dotenv()
### Initialize tools and agents ###
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
# serper_tool = NewSearchTool(SERPER_API_KEY)

try:
    query_gen = ProductQueryGenerator(
    )
    search_agent = SerperSearchAgent(
)
    
    extractor = PriceAvailabilityExtractor(
    role="",
    goal="",
    backstory=""
)
    
    change_detector = ChangeDetector(
    role="Change Detector",
    goal="",
    backstory=""
)

    
    advisor = PricingAdvisor(
    role="",
    goal="",
    backstory=""
)
    

    # Replace with your real SKUs and your own product price
    my_skus = [{"brand": "Acme", "model": "X100"}]
    my_price = 119.99
    old_competitor_data = []  # Load from DB or last run

    # Step 1: Generate Queries
    queries = query_gen.create_queries(my_skus)

    for query in queries:
        serp_results = search_agent.fetch_listings(query)
        competitor_data = extractor.extract(serp_results)
        changes = change_detector.compare(old_competitor_data, competitor_data)
        suggestions = advisor.suggest(my_price, changes)
        print(f"Query: {query}")
        print("Competitors found:", competitor_data)
        print("Changes:", changes)
        print("Suggestions:", suggestions)
        print('='*40)
except Exception as e:
    print(e)