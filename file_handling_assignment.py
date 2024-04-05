
file_path = "my_file.txt"

try:
    with open(file_path, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError:
    print(f"Error: Unable to read file '{file_path}'.")


# Python script to open "my_file.txt" in append mode ('a') and append three additional lines of text
file_path = "my_file.txt"

additional_lines = [
    "This is an additional line 1.\n",
    "This is an additional line 2.\n",
    "This is an additional line 3.\n"
]

try:
    with open(file_path, "a") as file:
        for line in additional_lines:
            file.write(line)
    print("Three additional lines appended successfully.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError:
    print(f"Error: Unable to open or write to file '{file_path}'.")
