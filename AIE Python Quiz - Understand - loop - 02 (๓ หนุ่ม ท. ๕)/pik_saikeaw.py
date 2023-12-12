def check_green_color(rgb_values):
    if all(0 <= value <= 255 for value in rgb_values):
        red, green, blue = rgb_values

        if green < (red+blue) :
            return "Not Green"
        elif green > red and green > blue:
            return "Green"
        else:
            return "Not Green"
    else:
        return "Value Out of Range"

rgb_str = input("RGB: ")
rgb_values = list(map(int, rgb_str.split(',')))
result = check_green_color(rgb_values)
print(result)
