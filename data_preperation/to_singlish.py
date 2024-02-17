from siconv import sinhala_to_singlish
import json

# Load the JSON file
with open('alpaca-sinhala.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate through each dictionary in the JSON data
for item in data:
    # Extract Sinhala text from the "input" field
    sinhala_instruction = item.get("instruction", "")
    sinhala_input = item.get("input", "")
    sinhala_output = item.get("output", "")

    # Convert Sinhala text to Singlish
    singlish_instruction = sinhala_to_singlish(sinhala_instruction)
    singlish_input = sinhala_to_singlish(sinhala_input)
    singlish_output = sinhala_to_singlish(sinhala_output)

    # Replace the original Sinhala text with the Singlish text
    item["instruction"] = singlish_instruction
    item["input"] = singlish_input
    item["output"] = singlish_output

# Save the modified JSON data in a new file called 'alpaca_data_sinhala.json'
with open('alpaca_data_sinhala.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("Conversion complete! Modified data saved in 'alpaca_data_sinhala.json'")

