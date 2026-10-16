# Example 1: Function with default parameter
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

"""
เขียน function ชื่อ convert_currency(value, currency)
ที่ทำหน้าที่ในการแปลงสกุล 
THB <-> USD กำหนดให้ 1 USD = 33 THB

ทั้งนี้ให้ function ดังกล่าว รับข้อมูล จำนวนเงินที่ต้องการแปลง และสกุลเงินปลายทาง

ตัวอย่างวิธีการเรียกใช้
convert_currency(100, "USD")
convert_currency(100, "THB")

ตัวอย่างหน้าจอ
100 THB = 3.33 USD
100 USD = 3300.0 THB
"""

def convert_currency(value, currency):
    result = 0
    if currency == "USD":
        result = value / 33.0
        print(f"{value} THB = {result} USD")
    else:
        result = value * 33.0
        print(f"{value} USD = {result} THB")

convert_currency(100, "USD")
convert_currency(100, "THB")