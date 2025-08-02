# main.py
from chameleon_agent import ChameleonAgent

def run_agent(role):
    print(f"🧠 Starting Chameleon Agent as {role.upper()}")

    agent = ChameleonAgent(role)

    while True:
        opponent_msg = input("\n👤 Opponent: ")
        if opponent_msg.lower() in ['exit', 'quit']:
            break

        reply = agent.negotiate(opponent_msg)
        print(f"🤖 Agent: {reply}")

if __name__ == "__main__":
    role = input("Enter role (buyer/seller): ").lower()
    run_agent(role)
