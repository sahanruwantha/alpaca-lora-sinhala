import json

new_data = []

with open('', 'r', encoding='utf-8') as file:
    data = json.load(file)

for entry in data:
    instruction = entry['instruction']
    input_value = entry.get('input', '') 
    output = entry['output']

    new_entry = {
        "instruction": instruction,
        "input": input_value,
        "output": output
    }

    new_data.append(new_entry)

new_json_file_path = 'modified_data.json'

with open(new_json_file_path, 'w', encoding='utf-8') as new_json_file:
    json.dump(new_data, new_json_file, ensure_ascii=False, indent=4)
