def check_brackets(br):
    stack = [] #สร้างลิสต์เปล่าของ Stack
    op_bracket = '({[' #กำหนดวงเล็บเปิด
    cl_bracket = ')}]' #กำหนดวงเล็บปิด
    bracket_pair = {')': '(', '}': '{', ']': '['} #สร้างDictionary

    for bracket in br:
        if bracket in op_bracket: #ถ้าวงเล็บเป็น op_bracket
            stack.append(bracket) #เพิ่มลงในลิสต์stack
        elif bracket in cl_bracket: #ถ้าวงเล็บเป็น cl_braket
            if not stack or stack.pop() != bracket_pair[bracket]: #ถ้าstackว่างหรือวงเล็บที่เหมือนกันไม่อยู่บนstack
                return "Not Equivalent" 

    if not stack: #ถ้าstackว่าง
        return "Equivalent"
    else:
        return "Not Equivalent"

# Input
input_string = input().strip() #รับค่า input

# Output
print("Bracket:", check_brackets(input_string))
