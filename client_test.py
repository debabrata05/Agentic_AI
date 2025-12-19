import requests

url = "http://localhost:8000/chat"

print("🤖 Waking up the agent...")

# Test 1: Complex logic using Custom MCP (Write file)
query = "Search online for the current price of Bitcoin. Then write a report called 'crypto_report.txt' with the price."
payload = {"query": query}

try:
    print(f"\nUser: {query}")
    response = requests.post(url, json=payload)
    print(f"Agent: {response.json()['response']}")
    
    print("-" * 20)

    # Test 2: Custom Math Tool
    query_2 = "I have data points: 10.5, 20.1, 5.5. Calculate the metrics for me."
    payload_2 = {"query": query_2}
    print(f"User: {query_2}")
    response_2 = requests.post(url, json=payload_2)
    print(f"Agent: {response_2.json()['response']}")

except Exception as e:
    print(f"Error: {e}")
    print("Is the server running? (python main.py)")
