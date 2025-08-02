# chameleon_agent.py
import random
from llama_api import call_llama_model

class ChameleonAgent:
    def __init__(self, role):
        self.role = role  # 'buyer' or 'seller'
        self.personas = ['Aggressive Trader', 'Smooth Diplomat', 'Data Analyst']
    
    def choose_persona(self):
        return random.choice(self.personas)

    def negotiate(self, opponent_message):
        current_persona = self.choose_persona()
        response = call_llama_model(opponent_message, current_persona)
        return response
