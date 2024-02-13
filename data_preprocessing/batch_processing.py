import json

# with open('data/without_code_alpaca_data_cleaned.json', 'r') as alpaca_data_cleaned_file, \
#         open('data/with_input_and_output.json', 'w') as with_input_and_output_file, \
#         open('data/without_input.json', 'w') as without_input_file:
    
#     alpaca_data_cleaned_json = json.load(alpaca_data_cleaned_file)
#     with_input_and_output_json = []
#     without_input_json = []

#     for alpaca_data_cleaned in alpaca_data_cleaned_json:
#         if alpaca_data_cleaned['input'] == "":
#             without_input_json.append(alpaca_data_cleaned)
#         else:
#             with_input_and_output_json.append(alpaca_data_cleaned)

#     json.dump(with_input_and_output_json, with_input_and_output_file, indent=4)
#     json.dump(without_input_json, without_input_file, indent=4)


with open('data/with_input_and_output.json', 'r') as json_file:
    data = json.load(json_file)

# Split the data into chunks of 100 objects each
chunk_size = 1000
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Write each chunk to separate JSON files
for i, chunk in enumerate(chunks):
    file_name = f"batches/2/{i + 1}.json"  # Naming files as 1.json, 2.json, etc.
    with open(file_name, 'w') as output_file:
        json.dump(chunk, output_file, indent=4)