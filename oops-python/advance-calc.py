import re 

database = []
position = -1

def calculate(expr):
    try: 
        match = re.fullmatch(r"\s*(-?\d+\.?\d*)\s*([\+\-\*/%**]{1,2})\s*(-?\d+\.?\d*)\s*", expr)

        if not match:
            print("Invalid expresion!")

        a = float(match.group(1))
        op = match.group(2)
        b = float(match.group(3))

        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        elif op == '/':
            return a/b
        elif op == '%':
            return a%b
        elif op == '**':
            return a**b
        else:
            print("Unsupported format")
    except Exception as e:
        return f"Error: {e}"       

while True:
    print("---- Advance Calculator ----")
    print("Enter expression like: 5 + 4 or 6*2")
    print("Use F (forward), B (backward), or Q (quit)")

    user_input = input(">> ").strip()

    if user_input.upper() == 'F':
        if position < len(database):
            position += 1
            print(f"Forwarded to: {database[position]}")

        else:
            print("Nothing to forward")
    elif user_input.upper() == 'B':
        if position > -1:
            position -= 1
            print(f"Backwards to: {database[position]}")
        else:
            print("Nothing to Back!")
    elif user_input.upper() == "Q":
        print("Exiting...")
        break
    else:
        result = calculate(user_input)

        if not result is None:
            database.append(f"{user_input} = {result}")
            position = len(database)-1
            print(f"Result: {result}")
