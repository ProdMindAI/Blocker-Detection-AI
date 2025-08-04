import requests

API_URL = "http://localhost:8000"

def get_root():
    try:
        response = requests.get(f"{API_URL}/")
        response.raise_for_status()
        print("Server response:", response.json())
    except requests.RequestException as e:
        print(f"Error during GET /: {e}")

def post_question():
    question = input("Enter your question for PMBuddy: ").strip()
    if not question:
        print("Question cannot be empty.")
        return
    payload = {"question": question}

    try:
        response = requests.post(f"{API_URL}/ask", json=payload)
        response.raise_for_status()
        data = response.json()
        print("\nPMBuddy's answer:")
        print(data.get("answer", "No answer received."))
    except requests.RequestException as e:
        print(f"Error during POST /ask: {e}")

def main():
    print("PMBuddy Client")
    while True:
        print("\nOptions:")
        print("1. Check server status (GET /)")
        print("2. Ask a question (POST /ask)")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            get_root()
        elif choice == "2":
            post_question()
        elif choice == "3":
            print("Exiting PMBuddy Client.")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
