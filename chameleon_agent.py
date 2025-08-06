# chameleon_agent.py
import random
from llama_api import call_llama_model

class ChameleonAgent:
    def __init__(self, role, min_price=None, max_price=None):
        self.role = role  # 'buyer' or 'seller'
        self.personas = ['Aggressive Trader', 'Smooth Diplomat', 'Data Analyst']
        self.min_price = min_price  # Only for seller
        self.max_price = max_price  # Only for buyer
        self.last_offer = None  # To track negotiation state

    def choose_persona(self):
        return random.choice(self.personas)

    def negotiate(self, opponent_message):
        current_persona = self.choose_persona()

        # Example decision-making logic
        if self.role == 'buyer':
            reply = self.buyer_logic(opponent_message, current_persona)
        else:
            reply = self.seller_logic(opponent_message, current_persona)

        return reply

    def buyer_logic(self, opponent_message, persona):
        # Simple offer generator (replace with real logic later)
        if not self.last_offer:
            self.last_offer = self.max_price - 1000
        else:
            self.last_offer -= 500  # Bargain downward

        return call_llama_model(
            f"I can offer ₹{self.last_offer} for your mangoes.", persona
        )

    def seller_logic(self, opponent_message, persona):
        # Simple price dropper
        if not self.last_offer:
            self.last_offer = self.min_price + 3000
        else:
            self.last_offer -= 1000  # Slowly come down

        return call_llama_model(
            f"My final offer is ₹{self.last_offer}. This is top-grade mangoes!", persona
        )
