def check_brackets(br):
    stack = []
    op_bracket = '({['
    cl_bracket = ')}]'
    bracket_pair = {')': '(', '}': '{', ']': '['}

    for bracket in br:
        if bracket in op_bracket:
            stack.append(bracket)
        elif bracket in cl_bracket:
            if not stack or stack.pop() != bracket_pair[bracket]:
                return "Not Equivalent"

    if not stack:
        return "Equivalent"
    else:
        return "Not Equivalent"

# Input
input_string = input().strip()

# Output
print("Bracket:", check_brackets(input_string))
