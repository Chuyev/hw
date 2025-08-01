from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79123456789"),
    Smartphone("iPhone", "15 Pro", "+79098765432"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79234567890"),
    Smartphone("Google", "Pixel 7", "+79345678901"),
    Smartphone("Huawei", "P50 Pro", "+79456789012")
]

for phone in catalog:
    print(f"{phone.brand} – {phone.model}. {phone.number}")
