import requests
import matplotlib.pyplot as plt

# API endpoint for retrieving nutrient information
api_url = "https://api.nal.usda.gov/fdc/v1/food/175139/nutrients"

# API key (replace with your own key)
api_key = "6a5iMwMmMEVvgaRCkSMoq7ZYJxosZc9dNfWj5h22"

# Request headers
headers = {
    "Content-Type": "application/json",
    "api_key": api_key
}

# Send GET request to retrieve nutrient information
response = requests.get(api_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract nutrient names and values
    nutrients = data["foods"][0]["foodNutrients"]
    nutrient_names = [nutrient["nutrientName"] for nutrient in nutrients]
    nutrient_values = [nutrient["value"] for nutrient in nutrients]
    
    # Create a bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(nutrient_names, nutrient_values)
    plt.xticks(rotation=90)
    plt.xlabel("Nutrient")
    plt.ylabel("Value")
    plt.title("Nutrient Values for Sardines")
    plt.tight_layout()
    plt.show()

else:
    print("Error: Unable to retrieve nutrient information.")
