import json
import re

def matches_regex(regex, text):
    return bool(re.compile(regex).search(text))

def contains_code(text):
    # filter based on keywords that indicate code
    code_blacklist = ['&&', '||', '<html>', ';\n', 'SELECT']
    
    return (
            any(code_keyword in text for code_keyword in code_blacklist) |
            matches_regex(r'\w+\(\w*\) \{', text) | # e.g. myFunc() {
            matches_regex(r'def \w+\(', text) | # e.g. def parse_list(
            matches_regex(r'\[A-z]+\.[A-z]+', text) | # e.g. this.language
            matches_regex(r': [\w\.#]{1,12};', text) | # e.g. font-size: 1.3em;
            matches_regex(r'<\/\w+>', text) # e.g. </html>
           )

def contains_words(text):
    return matches_regex(r'[A-z]{3,}', text) # words with at least three characters

def is_translatable(text):
    if text == "":
        return True # empty string won't be charged by DeepL
    return (contains_code(text) is False) and contains_words(text)

# Load JSON data from a file
with open('data/alpaca_data_cleaned.json', 'r') as file:
    data = json.load(file)

cleaned_data = []

for instruction in data:
    instruction_text = instruction['instruction']
    input_text = instruction['input']
    output_text = instruction['output']
    if (is_translatable(instruction_text) and is_translatable(input_text) and is_translatable(output_text)):
        cleaned_data.append(instruction)

# Write cleaned data to a new JSON file
with open('data/without_code_alpaca_data_cleaned.json', 'w') as json_file:
    json.dump(cleaned_data, json_file, indent=4)
