class Person():
    def __init__(self, name, date, phone, city, country,adress):
        self.name = name
        self._date = date
        self._phone = phone
        self.city = city
        self.country = country
        self._adress = adress

    def print_pablic_inf(self):
        show_pablic_inf = str(self.name) + self.city + " " + self.country
        return (self.name, self.city, self.country)

    def print_privat_inf(self):
        show_privat_inf = str(self.name + " " + self._date + " " + self._phone + " " + self.city + " " + self.country + " " + self._adress)
        return (self.name, self._date, self._phone, self.city, self.country, self._adress)

    def print_pablic_inf_1(self):
        return self.print_privat_inf()

homo = Person(
    "Ке́нни Макко́рмик",
    "24 of april",
    "0937225256",
    "Саус-парк",
    "USA",
    "South Park"
)

# print(homo.print_pablic_inf())
print(homo.print_pablic_inf_1())



