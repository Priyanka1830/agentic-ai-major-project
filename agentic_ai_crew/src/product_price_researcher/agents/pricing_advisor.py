from crewai import Agent

class PricingAdvisor(Agent):
    def suggest(self, my_price, competitor_data):
        suggestions = []
        for comp in competitor_data:
            suggestion = None
            if comp['price']:
                competitor_price = float(comp['price'].replace('$', ''))
                if competitor_price < my_price:
                    suggestion = f"Consider lowering price to ${competitor_price - 1:.2f} to remain competitive with {comp['seller']}."
                elif competitor_price > my_price:
                    suggestion = f"No action needed—your price (${my_price}) is lower than {comp['seller']} (${competitor_price})."
                suggestions.append(suggestion)
        return suggestions if suggestions else ["No price changes required."]
