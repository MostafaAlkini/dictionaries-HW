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

# Second question

def wordCount (s):
    words=s.split()
    dict={}
    for i in words:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    return dict

sentence=input("Enter a sentence: ")
print(wordCount(sentence))

# Third question

companyEmployees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}
print(companyEmployees)
companyEmployees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
print(companyEmployees)