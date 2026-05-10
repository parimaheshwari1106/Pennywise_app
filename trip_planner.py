# trip_planner.py
# Handles itinerary cost estimation

class TripPlanner:
    def __init__(self):
        self.costs = {}  # "transport": 0, etc.

    def set_cost(self, category, amount):
        self.costs[category] = amount

    def calculate_total(self):
        total = 0
        for key in self.costs:
            total = total + self.costs[key]
        return total
