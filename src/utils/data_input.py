def input_generator(input):
    """input is either a filename or a list of strings"""
    if isinstance(input, list):
        for line in input:
            yield line
    else:
        with open(input, "r") as f:
            for line in f:
                line = line.rstrip()
                yield line
