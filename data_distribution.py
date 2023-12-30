import json

with open('data/without_code_alpaca_data_cleaned.json', 'r') as file:
    data_file = json.load(file)

# Open the output files outside the loop to avoid repeated opening/closing
with open('data/to_translate_input.txt', 'w') as to_translate_input_file, \
        open('data/to_translate_instructions.txt', 'w') as to_translate_instructions_file, \
        open('data/to_translate_output.txt', 'w') as to_translate_output_file:

    for data in data_file:
        # Write 'input' data to to_translate_input.txt
        to_translate_input_file.write(data['input'])
        to_translate_input_file.write('\n')

        # Write 'instruction' data to to_translate_instructions.txt
        to_translate_instructions_file.write(data['instruction'])
        to_translate_instructions_file.write('\n')

        # Write 'output' data to to_translate_output.txt
        to_translate_output_file.write(data['output'])
        to_translate_output_file.write('\n')

# The files will be automatically closed after the 'with' blocks due to context management

