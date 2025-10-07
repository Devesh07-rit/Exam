def prompt_(filename):
  with open(filename,"w")as file:
    while true:
      line=input("Enter text(leave balnk to stop):")
      if line =="":
        breakfile.write(line + "\n")

  prompt_and_write("input.txt")