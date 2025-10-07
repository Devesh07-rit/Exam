def numbers():
    total_sum = 0   # keeps track of sum across all files

    while True:
        filename = input("Enter a filename (or press Enter to stop): ").strip()

        # stop if user enters empty string
        if filename == "":
            break

        try:
            with open(filename, "r") as file:
                file_sum = 0
                for line in file:
                    # split line into words, check if they are numbers
                    for word in line.split():
                        if word.isdigit():  # only sum integers
                            file_sum += int(word)

                print(f"Sum of numbers in {input.txt}: {file_sum}")
                total_sum += file_sum

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    print(f"Total sum of all numbers in all files: {total_sum}")
