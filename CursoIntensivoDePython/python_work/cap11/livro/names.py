from name_function import get_formatted_name


print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease giv me a firstname: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
