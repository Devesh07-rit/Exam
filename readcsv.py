def print_names(filename):
  with open(filename,"r") as file:
    #skip the header file
    next(file)
    for line in file:
      parts=line.strip().split(",")
      if len(parts) >=2:
        last_name = parts[0]
        first_name = parts[1]
        print(first_name,last_name)

  print_names("names.csv")