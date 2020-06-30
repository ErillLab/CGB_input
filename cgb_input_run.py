from cgb_input import create_file

input_file = 'pseudomonadales_test.json'

input_file = create_file(input_file)

with open('orthologs.json') as f:
    orth = json.load(f)
