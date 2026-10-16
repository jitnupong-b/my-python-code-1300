"""print("\n=== TRAVERSING STRINGS ===")
message = "hello"
index = 0

print("Method 1: Using for loop with enumerate")
for i, char in enumerate(message):
    print(f"message[{i}] = {char}")

print("\nMethod 2: Manual indexing")
index = 0
for char in message:
    print(f"message[{index}] = {char}")
    index += 1
"""






# เขียนโปรแกรม นับจำนวนอักขระที่สนใจในข้อความที่กำหนดโดยผู้ใช้
# 1. รับข้อความที่กำหนดให้จากผู้ใช้ (text)
# 2. รับอักขระที่สนใจจากผู้ใช้ (char)
# 3. แสดงผลการนับอักขระที่สนใจในข้อความออกทางหน้า

# ตัวอย่างหน้าจอ
# Insert the text: Kasetsart Sriracha
# Character to find: r
# 3 letters 'r' found in 'Kasetsart Sriracha'

"""print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text: ")
char = input("Character to find: ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")"""

# เขียนโปรแกรม ตรวจสอบความแข็งแรงของ password
# password ที่แข็งแรงคือ ยาวมากกว่า 8 ตัว และผสมกันระหว่างตัวเลข ตัวอักษร และอักขระพิเศษ

# ตัวอย่างหน้าจอ
# Insert your password: Test123
# Your password is not strong!

# Insert your password: Test1234;
# Your password is strong

password = input("Insert your password: ")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("Your password is strong!")
else:
    print("Your password is not strong!")