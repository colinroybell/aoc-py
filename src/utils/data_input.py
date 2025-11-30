def input_generator(input, terminate_with_empty=False):
    """input is either a filename or a list of strings"""
    if isinstance(input, list):
        for line in input:
            yield line
    else:
        with open(input, "r") as f:
            for line in f:
                line = line.rstrip()
                yield line
        if terminate_with_empty:
            yield ""
