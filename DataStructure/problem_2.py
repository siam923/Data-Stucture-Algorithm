import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path == '':
        return 'No path provided'

    out = []
    if not os.path.isdir(path) :
        if path.endswith(suffix):
            return [path]
        return []
    for i in os.listdir(path):
        if os.path.isfile(i) and i.endswith(suffix):
            out.append(os.path.join(path,i))
        else:
            out = out + find_files(suffix, os.path.join(path,i))
    return out

path = './testdir'
test_1 = find_files('c',path)
for i in test_1:
    print(i)

test_2 = find_files('java', path)
print(test_2) # []

test_3 = find_files('', '') 
print(test_3) # no path provided
