def numbers():
    total_sum = 0  # To store sum from all valid files

    while True:
        filename = input("Enter a filename (or press Enter to quit): ")
        if filename == "":
            break  # stop when user enters empty string

        try:
            with open(filename, "r") as file:
                file_sum = 0
                for line in file:
                    file_sum += float(line.strip())
                print(f"Sum of numbers in {filename}: {file_sum}")
                total_sum += file_sum

        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")

        except ValueError:
            print(f"Error: '{filename}' contains invalid data. Only numbers are allowed.")

    print(f"\nTotal sum of numbers from all valid files: {total_sum}")