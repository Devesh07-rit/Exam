def search_word(filename):
  found = False 
  for line in f.read().spilt():
    #if line.strip().lower() == word.lower():
    if line.strip() == word:
      found = true 
      break
    f.close()
    if found:
      print("Word Found!")
    else:
      print("Word not found.")
      search_word("input.txt")

    