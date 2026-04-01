import json
import requests
#requests is a synchronous HTTP client library. It blocks execution until the HTTP response is received.
url="https://services.odata.org/Experimental/Northwind/Northwind.svc/Products(1)"
response = requests.get(url)

print(f"the response status is {response.status_code}")
print(f"the response content is {response.text}")
parsed_json = json.loads(response.text)
productName=parsed_json["ProductName"]
print(f"the name of the product is {productName}")