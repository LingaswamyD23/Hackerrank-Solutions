import re

def convertion(input_str, command):
    if command == 'M' or command == 'V':  # method #variable
        return "".join(str(i) if idx == 0 else str(i).capitalize() for idx, i in enumerate(input_str.split(" ")))
    elif command == 'C':  # Class
        return "".join(str(i).capitalize() for i in input_str.split(" "))


def camel(opperation, command, text):
    # out = re.split("([A-Z][^A-Z]*)", re.sub('[()!@#$]', '', opt[2]))
    if opperation == 'S':  # Split
        if command == 'C' or command == 'V':
            out = re.split("([A-Z][^A-Z]*)", text)
        elif command == 'M':
            out = re.split("([A-Z][^A-Z]*)", re.sub('[()!@#$]', '', text))
        # print(out)
        # line = re.sub('[()!@#$]', '', opt[2])
        print(" ".join(str(item.lower()) for item in out if item !=''))
    elif opperation == 'C':  # Combine
        if command == 'M':  # method
            print(convertion(text, command) + "()")
        elif command == 'C':  # Class
            print(convertion(text, command))
        elif command == 'V':  # variable
            print(convertion(text, command))


if __name__ == '__main__':
    while True:
        try:
            opperation, command, text = input().rstrip(('\n\r')).split(";")
            camel(opperation, command, text)
        except EOFError:
            break
    
        
