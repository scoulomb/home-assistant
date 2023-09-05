import requests
# pip3 install requests 


# Replace {pin} and {port} with the actual values
pin = ""
port = "8443"

# Define the base URL for the Somfy TaHoma local API
base_url = f"https://gateway-{pin}.local:{port}/enduser-mobile-web/1/enduserAPI"

# Disable certificate verification (insecure)
verify_ssl = False

bearer_token=""


# Define the event listener registration endpoint
register_endpoint = f"{base_url}/events/register"

# Define the event fetching endpoint
fetch_endpoint = f"{base_url}/events/{{listenerId}}/fetch"



def register_event_listener():
    # Send a POST request to register an event listener with the bearer token
    headers = {'Authorization': f"Bearer {bearer_token}"}
    print(headers)
    response = requests.post(register_endpoint, headers=headers, verify=verify_ssl)
    print(response.text)
    if response.status_code == 200:
        listener_id = response.json().get("id")
        return listener_id
    else:
        return None

def fetch_event(listener_id):

    # Fetch an event using the registered listener ID and the bearer token
    fetch_url = fetch_endpoint.format(listenerId=listener_id)
    headers = {'Authorization': f"Bearer {bearer_token}"}
    response = requests.post(fetch_url, headers=headers, verify=verify_ssl)
    print(response.text)
    if response.status_code == 200:
        events = response.json()
        return events
    else:
        return None

def main():
    # Register an event listener
    listener_id = register_event_listener()
    if listener_id:
        print(f"Event listener registered with ID: {listener_id}")
        import time
        time.sleep(10) # <- trigger command here

        # Fetch an event
        events = fetch_event(listener_id)
        print(events)
        if events:
            if events:
                print("Fetched event:")
                print(events[0])  # Print the first event
            else:
                print("No events available.")
        else:
            print("Failed to fetch events.")
    else:
        print("Failed to register event listener.")

if __name__ == "__main__":
    main()
