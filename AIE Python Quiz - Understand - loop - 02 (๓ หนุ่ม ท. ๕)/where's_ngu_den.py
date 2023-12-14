def find_snake_location(path):
    x, y = 0, 0 #ตำแหน่งเริ่มต้น

    snake_locations = [] #สร้างลิสต์เปล่า

    for move in path: #เพิ่มลดค่าตามทิศทาง
        if move == '^':
            y += 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == 'v':
            y -= 1
        elif move == 'x':
            snake_locations.append((x, y)) #เพิ่มตน.ปัจจุบันลงในลิสต์

    if not snake_locations: #ตรวจว่ามีตำแหน่งของงูไหม
        return 'Not Found'
    else: #ถ้ามีตำแหน่งของงูก็ปริ้น
        return snake_locations

path = input("Path: ") #ใส่ทิศทางของงู
locations = find_snake_location(path) #เรียกใช้ฟังก์ชัน
    
if locations != 'Not Found':
    new_tup = ' '.join([str(tuple(map(int, i))) for i in locations])
    print("Locations:",new_tup) #แสดงผลลัพธ์แบบtuple
else:
    print(locations)
print()
