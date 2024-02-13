import json

def convert_to_json(input_text):
    entries = []
    current_entry = {}

    for line in input_text.splitlines():
        if line.startswith("Translated Instruction:"):
            if current_entry:
                entries.append(current_entry)
            current_entry = {"instruction": line.split(":")[1].strip()}
        elif line.startswith("Translated Input:"):
            current_entry["input"] = line.split(":")[1].strip()
        elif line.startswith("Translated Output:"):
            current_entry["output"] = line.split(":")[1].strip()

    if current_entry:
        entries.append(current_entry)

    return json.dumps(entries, ensure_ascii=False)

# Read the content of your text file
with open('../batches/translated-final/combined_file.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

# Convert to JSON format
json_result = convert_to_json(input_text)

with open('data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_result)

print("Conversion completed. Output saved as data.json.")


