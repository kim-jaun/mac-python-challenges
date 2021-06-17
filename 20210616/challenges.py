"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

def add_to_dict(add_arg, add_arg2, add_arg3 = ""):
  if type(add_arg) == dict:
    if add_arg3 != "":
      if add_arg2 in add_arg:
        print(f"{add_arg2} is already on the dictionary. Won't add.")
      else:
        add_arg[add_arg2] = add_arg3
        print(f"{add_arg2} had been added.")
    else:
      print("You need to send a word an d a definition.")
  else:
    print(f"You need to send a dictionary. You sent: {type(add_arg)}")
  pass

def get_from_dict(get_arg, get_arg2=""):
  if type(get_arg) == dict:
    if get_arg2 != "":
      if get_arg2 in get_arg:
        print(f"{get_arg2}: {get_arg[get_arg2]}")
      else:
        print(f"{get_arg2} was not found in this dict.")
    else:
      print("You need to send a word to search for.")
  else:
    print(f"You need to send a dictionary. You sent: {type(get_arg)}")
  pass

def update_word(word_arg, word_arg2, word_arg3 = ""):
  if type(word_arg) == dict:
    if word_arg3 != "":
      if word_arg2 in word_arg:
        print(f"{word_arg2} has been updated to: {word_arg3}")
        word_arg[word_arg2] = word_arg3
      else:
        print(f"{word_arg2} is not on the dict. Can't update non-existing word.")
    else:
      print("You need to send a word and a definition to update.")
  else:
    print(f"You need to send a dictionary. Ypu sent: {type(word_arg)}")
  pass

def delete_from_dict(del_arg, del_arg2 = ""):
  if type(del_arg) == dict:
    if del_arg2 != "":
      if del_arg2 in del_arg:
        print(f"{del_arg2} has been deleted.")
        del del_arg[del_arg2]
      else:
        print(f"{del_arg2} is not in this dict. Won't delete.")
    else:
      print("You need to specify a word to delete.")
  else:
    print(f"You need to send a dictionary. You sent: {type(del_arg)}")
  pass

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\