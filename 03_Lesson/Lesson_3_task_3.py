from address import Address
from mailing import Mailing

to_address = Address(188352, "г.Гатчина", "ул. Чкалова", "дом 13", "квартира 55")
from_address = Address(198320, "г.Красное Село", "ул. Бронетанковая", "дом 11", "квартира 74,")
mailing = Mailing(to_address, from_address, 500, "от первой платформы")

print(mailing)
