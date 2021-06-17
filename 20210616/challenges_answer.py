def add_to_dict(a_dict, word="", definition=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == '' or definition == '':
    print("You need to send a word and a definition.")
  else:
    if word in a_dict:
      print(f"{word} is already on the dictionary. Won't add.")
    else:
      a_dict[word] = definition
      print(word,"has been added.")


def get_from_dict(a_dict, word=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == '':
    print("You need to send a word to search for.")
  else:
    if word not in a_dict:
      print(f"{word} was not found in this dict.")
    else:
      print(f"{word}: {a_dict[word]}") 


def update_word(a_dict, word="", definition=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == "" or definition == "":
    print("You need to send a word and a definition to update.")
  else:
    if word not in a_dict:
      print(f"{word} is not on the dict. Can't update non-existing word.")
    else:
      a_dict[word] = definition
      print(word, "has been updated to:", definition)


def delete_from_dict(a_dict, word=""):
  if type(a_dict) is not dict:
    print("You need to send a dictionary. You sent:", type(a_dict))
  elif word == "":
    print("You need to specify a word to delete.")
  else:
    if word not in a_dict:
      print(f"{word} is not in this dict. Won't delete.")
    else:
      del a_dict[word]
      print(f"{word} has been deleted.")
