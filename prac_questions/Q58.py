def find_and_display_numbers(input_string):
    # Function to find numbers in the given string and store them in a list
    numbers_list = list(map(int, filter(lambda x: x.isdigit(), input_string.split())))

    # Find numbers longer than the length of the list
    longer_numbers = sorted(filter(lambda x: len(str(x)) > len(numbers_list), numbers_list))

    # Display longer numbers in sorted form
    if longer_numbers:
        print("Numbers longer than the length of the list in sorted form:", longer_numbers)
    else:
        print("No numbers longer than the length of the list found.")

# Input a string
input_string = input("Enter a string containing numbers: ")

# Find and display numbers longer than the length of the list
find_and_display_numbers(input_string)
