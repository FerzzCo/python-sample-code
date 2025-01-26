import requests

# URL of the Flash Call service
url = "https://flash-call.liara.run/services/call/call/"

# Request body payload
payload = {
    "destination": "0930xx16xxx",  # The phone number you want to call
    "token": "Ih.nMOjBa3WystRfdnnFzsmt.foqm0O7gFBAm"  # The access token for the service
}

# Send a POST request
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    print("Call initiated successfully!")
    print("Server response:", response.json())  # Display the server response
else:
    print("Failed to initiate the call!")
    print("Status code:", response.status_code)
    print("Server response:", response.text)  # Display the error message