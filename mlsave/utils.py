import re
from os.path import splitext

def splitNumericTail(string):
    suffix = re.split('[^\d]', string)[-1]
    return string[:-len(suffix)], suffix


def endsWithNumber(string):
    return bool(splitNumericTail(string)[-1])


def increm(string):
    filename, file_extension = splitext(string)
    if not endsWithNumber(filename):
        return filename + "2" + file_extension
    else:
        prefix, suffix = splitNumericTail(filename)
        return prefix + str(int(suffix) + 1) + file_extension

if __name__ == '__main__':
    pass
