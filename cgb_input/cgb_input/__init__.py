from cgb_input import cgb_input_main

def create_file(json_file):
    """
    'middle man' function to create a layer of abstraction betweeen end user and main source code
    """
    final = cgb_input_main(json_file)

    return final


