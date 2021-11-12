import requests
import json

how_many_facts = int(input("How many dog facts you want to see? "))

params = {
    "number": how_many_facts
}
get_json = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs", params)

try:
    content = get_json.json()
except json.decoder.JSONDecodeError:
    print("Invalid format. Check resource address.")
else:
    print("=======================================")
    for element in content:
        print("*", element["fact"])
    print("=======================================")

input('Press ENTER to exit')
