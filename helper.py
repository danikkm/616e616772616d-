def trim(string_to_trim):
    return "".join(string_to_trim.split())

def read_words(fname):
    print('Loading file... ')
    f = open(fname, 'r')
    lines = f.read().splitlines()
    f.close()
    print("Done!")
    return lines
