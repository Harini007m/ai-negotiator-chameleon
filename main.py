import time
from agent import ChameleonAgent

def run_agent(role):
    print(f"🧠 Starting Chameleon Agent as {role.upper()}")
    
    if role == "buyer":
        max_budget = int(input("Enter your MAX budget (₹, no commas): "))
        agent = ChameleonAgent(role="buyer", max_budget=max_budget)
    elif role == "seller":
        min_price = int(input("Enter your MIN price (₹, no commas): "))
        agent = ChameleonAgent(role="seller", min_price=min_price)
    else:
        print("Invalid role. Please choose 'buyer' or 'seller'.")
        return

    start_time = time.time()
    fallback_sent = False

    while True:
        opponent_msg = input("\n👤 Opponent: ")

        # Check 3-minute limit
        elapsed = time.time() - start_time
        if elapsed > 180:
            print("\n⏰ Time's up! No deal was made.")
            break

        response = agent.generate_response(opponent_msg)

        if response == "FALLBACK":
            print("🤖 Agent (Fallback): Final offer made due to timeout risk.")
            break
        else:
            print(f"🤖 Agent: {response}")

