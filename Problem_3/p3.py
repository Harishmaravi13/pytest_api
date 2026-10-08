import requests
url = "https://dummyjson.com/users/add"
data = {
    "firstName": "John",
    "lastName": "Smith",
    "age": 25,
    "email": "john@example.com"
}
response = requests.post(url,json = data)
create= response.json()
print("Create User")
print("******************")

print(f"Status Code: {response.status_code}")

id_check = "id" in create
fname_check = create.get("firstName") == "John"
lname_check =create.get("lastName") == "Smith"
age_check = create.get("age") == 25
status_check = response.status_code ==201

print(f"User ID : {'PASS' if id_check else 'FAIL'}")
print(f"First Name : {'PASS' if fname_check else 'FAIL'}")
print(f"Last Name : {'PASS' if lname_check else 'FAIL'}")
print(f"Age : {'PASS' if age_check else 'FAIL'}")

user_id = create.get("id")
print("User ID:", user_id)

updated_url= f"https://dummyjson.com/users/1"
print("Update URL:", updated_url)
updated_data={"age":30}
updated_response = requests.put(updated_url,json = updated_data)
new_data=updated_response.json()


print("Update User")
print("**************")
print(f"Status Code : {updated_response.status_code}")

update_status_check = updated_response.status_code == 200

age_updated_check = new_data.get("age") == 30

print(f"Age Updated : {'PASS' if age_updated_check else 'FAIL'}")

overall = all([status_check,id_check,fname_check,lname_check,age_check,update_status_check,age_updated_check])

print("\nOverall Result:", "PASS" if overall else "FAIL")