import json

productFileName = "./resources/product.json"
with open(productFileName, "r") as file:
    product = json.load(file)
    for key, value in product.items():
        print(f"{key}: {value}")

with open(productFileName, "r") as file:
    productJson = file.read()
    product = json.loads(productJson)
    for key, value in product.items():
        print(f"{key}: {value}")

employee = {
    "age": 65,
    "gender": "male",
    "department": {
        "name": "Engineering"
    },
    "doj": "2020-01-30T00:00:00+00:00",
    "dob": "2000-01-30T00:00:00+00:00",
    "lob": ["SuccessFactors"]
}
employeeFileName = "./resources/employee.json"
with open(employeeFileName, 'w') as file:
    json.dump(employee, file)
