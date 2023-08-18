import requests

API_KEY = '6a5iMwMmMEVvgaRCkSMoq7ZYJxosZc9dNfWj5h22'
FOOD_ID = '35814'  # USDA Food ID for generic canned sardines

# Construct the API URL
url = f"https://api.nal.usda.gov/fdc/v1/food/{FOOD_ID}?api_key={API_KEY}"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    food = data['food']

    # Extract and print nutritional facts
    nutrients = food['foodNutrients']
    print("Nutritional Facts for Sardines:")
    for nutrient in nutrients:
        name = nutrient['nutrient']['name']
        value = nutrient['amount']
        unit = nutrient['nutrient']['unitName']
        print(f"{name}: {value} {unit}")

else:
    print("Error:", response.status_code)
