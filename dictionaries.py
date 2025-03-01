# Create a function that take to parameter
def combineDictionaries(fd,sd):
    for key in fd:
        if key in sd:
            fd[key]=sd[key]

    for key in sd:
        if key not in fd:
            fd[key]=sd[key]
    print(fd)
    return fd

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 10, "d": 4}

combineDictionaries(dict1,dict2)
