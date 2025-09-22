#1.String Manipulation
def capitalize_words():
    name = input("TYPE IN YOUR SENTENCE: ")
    cap_name = name.title()
    print(f'{cap_name}')
capitalize_words()


#2.List Methods
my_list=[]
count=int(input("HOW MANY NUMBERS DO YOU WANT TO INPUT"))
for i in  range(count):
    num=int(input(f"ENTER NUMBER {i+1} : "))
    my_list.append(num)
print("Your final list is", my_list)
double_list= []
for i in my_list:
    double=i+i
    double_list.append(double)
print("Your final list is", double_list)
sumodd=0
for i in double_list:
    if i % 2 != 0:
        sumodd=i+sumodd
print(f"(The sum of remaining numbers is {sumodd}")


#Question 3: Dictionary Unpacking Equivalent
def extraction_users(user):
    username=user["profile"]["username"]
    email=user["profile"]["email"]
    theme=user["settings"]["theme"]
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Theme: {theme}")
user = {
    "id": 1,
    "profile": {
        "username": "mandem",
        "email": "mandem@example.com"
    },
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}
extraction_users(user)




#4.List of Dictionaries
budget=int(input("WHAT IS YOUR BUDGET?"))
def get_affordable_products(products, budget):
    for product in products:
        if product["price"] <= budget:
            print(f"THE PRICE OF {product['name']} is  {product['price']}")

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600}
]
get_affordable_products(products, budget)





# Question 5: *args and Set Union
def merge_lists(*lists):
    combined = []
    for i in lists:
        combined.extend(i)
    unique_list = list(set(combined))
    return unique_list
print(merge_lists([1, 2], [2, 3], [3, 4]))





# Question 6: Sorting & Finding
def second_largest(nums):
    largest = max(nums)
    nums.remove(largest)
    second = max(nums)
    return second
print(second_largest([10, 5, 8, 20, 15])) 






#Question 7: Higher Order Functions
def apply_operation(lst, operation):
    result = [] 
    for num in lst:
        if operation == "square":
            result.append(num ** 2)
        elif operation == "double":
            result.append(num * 2)
        elif operation == "negate":
            result.append(-num)
        else:
            raise ValueError("Unknown operation!")  
    return result
print(apply_operation([1, 2, 3], "square"))  
print(apply_operation([1, 2, 3], "negate"))  
print(apply_operation([1, 2, 3], "double"))




#Question 8: Advanced Dictionary Manipulation
def group_by_category(items):
    grouped = {}
    for item in items:
        category = item["category"]
        name = item["name"]
        if category in grouped:
            grouped[category].append(name)
        else:
            grouped[category] = [name]
    return grouped
items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"}
]
print(group_by_category(items))




#Question 9: Default & Safe Access 
def get_user_city(user):
    if "address" in user and "city" in user["address"]:
        return user["address"]["city"]
    else:
        return "Unknown"
user1 = {"name": "John", "address": {"city": "Lagos"}}
user2 = {"name": "Mary"}
print(get_user_city(user1))  
print(get_user_city(user2))  




#Question 10 (Bonus: Async + HTTP Request) 
import asyncio
import aiohttp

async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/posts") as response:
            data = await response.json()  # convert response to Python list/dict
            for post in data[:5]:  # take first 5 posts
                print(post["title"])
asyncio.run(fetch_posts())
