import json
import requests

url="https://services.odata.org/Experimental/Northwind/Northwind.svc/Products(1)"
response = requests.get(url)

print(f"the response status is {response.status_code}")
print(f"the response content is {response.text}")
parsed_json = json.loads(response.text)
productName=parsed_json["ProductName"]
print(f"the name of the product is {productName}")