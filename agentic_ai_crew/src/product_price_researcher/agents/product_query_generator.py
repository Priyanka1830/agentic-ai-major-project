from crewai import Agent

class ProductQueryGenerator(Agent):
    def create_queries(self, sku_list):
        queries = []
        for sku in sku_list:
            queries.append(f"{sku['brand']} {sku['model']} buy")
            queries.append(f"best price {sku['brand']} {sku['model']}")
        return queries
