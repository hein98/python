data = {0: 34, 1: 35, 2: 67, 3: 8}
print(type(data))

print(data[0])
print(data.get("wgesd", "not found"))

# in dictonary , keys are sets and values are lists

# combining keys and values

keys = {1, 2, 3}
vals = {"a", "b", "c"}

dict1 = dict(zip(keys, vals))
print(dict1)

###########

data = {
    "js": "vscode",
    "python": ["vscode", "pycharm"],
    "java": {"core": "vscode", "spring": "iij"},
}

print(data['java']['core'])
