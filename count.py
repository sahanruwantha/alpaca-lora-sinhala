import json

with open('data/without_code_alpaca_data_cleaned.json', 'r') as file:
    data = json.load(file)
    characters_count = len(data)
    print("Total characters in the JSON object:", characters_count)
