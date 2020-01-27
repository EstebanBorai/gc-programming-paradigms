def remove_characters(string, unwanted_character_list):
  "Takes unwanted characters as a list and removes them from a string"
  out_string = ''

  for character in string:
    if character not in unwanted_character_list:
      out_string += character

  return out_string
