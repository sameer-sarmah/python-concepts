import asyncio
import aiohttp
import httpx

async def fetch_product():
    url = "https://services.odata.org/Experimental/Northwind/Northwind.svc/Products(1)"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"the response status is {response.status}")
            text = await response.text()
            print(f"the response content is {text}")
            parsed_json = await response.json()
            product_name = parsed_json["ProductName"]
            print(f"the name of the product is {product_name}")

async def fetch_product_httpx():
    url = "https://services.odata.org/Experimental/Northwind/Northwind.svc/Products(1)"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"$format": "application/json"})
        print(f"the response status is {response.status_code}")
        print(f"the response content is {response.text}")
        parsed_json = response.json()
        product_name = parsed_json["ProductName"]
        print(f"the name of the product is {product_name}")

if __name__ == "__main__":
    asyncio.run(fetch_product())
    asyncio.run(fetch_product_httpx())
