from google.cloud import translate_v2 as translate
import json

# Replace 'your_project_key.json' with your service account key file


key_file = ''

# Instantiate a client
client = translate.Client.from_service_account_json(key_file)

# Language code for translation (e.g., 'es' for Spanish, 'fr' for French, etc.)
target_language = 'si'  # Translate to Sinhala

# List to store translated data
translated_data = []

# Replace 'path_to_your_json_file' with the actual path to your JSON file
file_path = "data/with_input_and_output.json"
# Open the JSON files and load their contents

data_to_translate = []

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

# Translate each item in the data
for entry in data:
    translated_entry = {
        "instruction": client.translate(entry["instruction"], target_language=target_language)["translatedText"],
        "input": client.translate(entry["instruction"], target_language=target_language)["translatedText"],
        "output": client.translate(entry["output"], target_language=target_language)["translatedText"]
    }
    print(translated_entry)
    translated_data.append(translated_entry)

# Define the path to save the translated data as a text file
save_to = 'batches/translated/1/12.txt'  # Updated folder structure for multiple batches

# Write translated data to a text file
with open(save_to, 'w', encoding='utf-8') as output_file:
    for entry in translated_data:
        output_file.write(f"Translated Instruction: {entry['instruction']}\n")
        output_file.write(f"Translated Output: {entry['output']}\n")
        output_file.write("--------------------------------------------\n")

# Display a confirmation message
print(f'Translated data saved to {save_to}')
