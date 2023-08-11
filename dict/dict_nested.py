
# A dictionary can contain dictionaries called nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

dict1 = {
    "name" : "Emil",
    "year" : 2004
}

dict2 = {
    "name" : "Tobias",
    "year" : 2007
}

dict3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily2 = {
    "child1" : dict1,
    "child2" : dict2,
    "child3" : dict3,
}

print("\n\n\n")
print(myfamily2)

## How to access nested diction items
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
  "child4" : {
    "name" : "Linus",
    "year" : 2011,
    "child" : {
        "age" : 10
    }
  }
}

print(f'Name of child 1: {myfamily["child1"]["name"]}')
print(myfamily["child3"]["year"])
print(myfamily["child4"]["child"]["age"])
