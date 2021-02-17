import re
from os.path import splitext
from pkg_resources import working_set


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

def get_installed_packages():
    return (i.key for i in working_set)

if __name__ == '__main__':
    pass
