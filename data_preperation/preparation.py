import json

new_data = []

# Load the JSON file
with open('/home/sahan/Desktop/alpaca-lora-sinhala/data/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate over each entry in the JSON file
for entry in data:
    instruction = entry['instruction']
    input_value = entry.get('input', '')  # Use get() method to avoid KeyError
    output = entry['output']

    new_entry = {
        "instruction": instruction,
        "input": input_value,
        "output": output
    }

    new_data.append(new_entry)

# Create a new JSON file for saving the modified data
new_json_file_path = 'modified_data.json'

# Save the modified data to the new JSON file
with open(new_json_file_path, 'w', encoding='utf-8') as new_json_file:
    json.dump(new_data, new_json_file, ensure_ascii=False, indent=4)
