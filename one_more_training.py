# fh = open('text.txt', 'w+')
# fh.write('Another new text. \nOne more line. \nNot finished yet')
# fh.seek(2)
# fh.read(3)
# position = fh.tell()
# print(position)
# fh.close

# fh = open ('text.txt','r')
# lines = [el.strip() for el in fh.readlines()]
# print(lines)
# fh.close()
# with open('text.txt', 'w') as fh:
#     fh.write('One more new unique file \n not so fast \n haven"t finished yet')
# with open('text.txt','r') as fh:
#     lines = [el.strip() for el in fh.readlines()]
# print(lines)
# with open('raw_data.bin','wb') as fh:
#     fh.write(b'Hello world!')
    
# byte_string = b'Hello world!'
# Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# # byte_numbers = bytes(numbers)
# # print(byte_numbers)  # Виведе байтове представлення чисел
# s = "Привіт!"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
