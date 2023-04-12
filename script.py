import random
import time

def generate_product_key():
    year_start = 1995
    year_end = 2003
    oem = "OEM"
    product_keys = []

    for i in range(30):
        year = str(random.randint(year_start, year_end) % 100).zfill(2)
        day = str(random.randint(1, 366)).zfill(3)
        nnnnnnn = str(random.randint(0, 999999)).zfill(7)
        while sum(int(digit) for digit in nnnnnnn) % 7 != 0:
            nnnnnnn = str(random.randint(0, 999999)).zfill(7)
        zzzzz = str(random.randint(0, 99999)).zfill(5)
        product_key = f"{day}{year}-{oem}-{nnnnnnn}-{zzzzz}"
        product_keys.append(product_key)

    return product_keys

def main():
    product_keys = generate_product_key()
    for key in product_keys:
        print(key)

if __name__ == "__main__":
    main()

input("Press enter key to exit...")