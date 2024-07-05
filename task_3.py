def are_brackets_symmetrical(input_string):
    stack = []
    opening_brackets = set("({[")
    closing_brackets = set(")}]")
    matches = {")": "(", "}": "{", "]": "["}
    
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != matches[char]:
                return "Несиметрично"
            stack.pop()
    
    return "Симетрично" if not stack else "Несиметрично"

# Приклади
test_strings = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for s in test_strings:
    print(f"{s}: {are_brackets_symmetrical(s)}")
