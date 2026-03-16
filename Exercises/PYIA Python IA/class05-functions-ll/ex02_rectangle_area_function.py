def calculate_area_rectangle(width, length):
    return width * length

wid = float(input('Insert the width: '))
leng = float(input('Insert the length: '))

area = calculate_area_rectangle(wid, leng)

print(f'Area of rectangle: {area}')