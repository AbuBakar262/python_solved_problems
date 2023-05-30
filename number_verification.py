import requests
apiKey = "52b1dd7e81394e9397077cf288a3f240&phone=14152007986"
apiUrl = "https://phonevalidation.abstractapi.com/v1/?"
phno = input("Enter Phone Number: ")
url = apiUrl + "api_key=" + apiKey + "&number=" + phno
response = requests.get(url)
print("Phone No Details: ", response.json())