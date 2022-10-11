# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open("Task5_RLE\Task_5(1)_RLE.txt", 'r') as data:
    my_text = data.read()
    
def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code +=(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

str_code = encode_rle(my_text)
print(str_code)
dev_12 = str_code

with open("Task5_RLE\Task5(2)_RLE_encod.txt", "w") as data:
    data.write(dev_12)
        
    