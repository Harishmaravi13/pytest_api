import requests
print("Product API Test")
print("*********************")
url = "https://dummyjson.com/products"
response= requests.get(url)
retrive= response.json()

print(f"Status Code : {response.status_code}")

product_field_check= "products" in retrive
print(f"Products Field: {'PASS' if product_field_check else 'FAIL'}")
product_count = len(retrive["products"]) > 10
print(f"Product Count: {'PASS' if product_count else 'FAIL'}")

for product in retrive["products"]:
    product_stucture=(
        "id" in product and "title" in product and "price" in product and "category" in product
    )
print(f"Product Structure: {'PASS' if product_stucture else 'FAIL'}")
products = retrive["products"]

highest = products[0]
lowest = products[0]

for product in products:
    if product["price"] > highest["price"]:
        highest = product

    if product["price"] < lowest["price"]:
        lowest = product

print("\nHighest Price:")
print(f"Product : {highest['title']}")
print(f"Price   : ${highest['price']}")

print("\nLowest Price:")
print(f"Product : {lowest['title']}")
print(f"Price   : ${lowest['price']}")

overall = all([product_field_check,product_stucture,product_count])
print(f"Overall: {'PASS' if overall else 'FAIL'}")