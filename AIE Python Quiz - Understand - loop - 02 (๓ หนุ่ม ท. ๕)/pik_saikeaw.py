def check_green_color(rgb_values):
    if all(0 <= value <= 255 for value in rgb_values): #ถ้ามีค่าอยู่ในช่วง 0,255
        red, green, blue = rgb_values

        if green < (red+blue) : #ถ้าสีเขียวน้อยกว่าผลรวมของสีแดงและสีน้ำเงิน
            return "Not Green"
        elif green > red and green > blue: #ถ้าสีเขียวมีค่ามากกว่าสีแดงและสีน้ำเงิน
            return "Green"
        else:
            return "Not Green"
    else: #ถ้ามีค่าที่อยู่นอกช่วง0, 255
        return "Value Out of Range"

rgb_str = input("RGB: ") #รับค่า input
rgb_values = list(map(int, rgb_str.split(','))) #แปลงข้อมูลให้เป็นจำนวนเต็ม
result = check_green_color(rgb_values) #เรียกใช้function
print(result)
