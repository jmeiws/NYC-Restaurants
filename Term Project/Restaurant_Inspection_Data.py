import requests
import json

def restaurant_data():
    Restaurant_inspection_api_data = 'https://data.cityofnewyork.us/resource/4dx7-axux.json'
    response = requests.get(url=Restaurant_inspection_api_data)

    if response.status_code == 200:
        data = response.json()
        json_data = json.dumps(data, indent = 4)
        #print (json_data)
        return json_data
    else: 
        print("Failed to retive data from the API. Status Code: ", response.status_code)
    

def data_on_specific_borough():
    data = json.loads(restaurant_data())  # Assuming restaurant_data() retrieves JSON data as a string
    input_borough = input("Input the Borough: ")

    # Filter entries where "borough" matches the input
    filtered_entries = [entry for entry in data if entry.get("borough") == input_borough]

    # Extract restaurant names from filtered entries and print them
    restaurant_names = [entry["restaurantname"] for entry in filtered_entries]
    print("Restaurant Names in", input_borough, "Borough:", restaurant_names)

    return restaurant_names
