class City():
    def __init__(self, name_city, name_state, count_user, code_phone, code_city, country):
        self.name_city = name_city
        self._name_state = name_state
        self._count_user = count_user
        self._code_phone = code_phone
        self._code_city = code_city
        self.country = country

    def print_pablic_inf(self):
        show_pablic_inf = str(self.name_city + " " + self.country)
        return (self.name_city,  self.country)

    def print_privat_inf(self):
        show_privat_inf = str(self._name_state + " " + self._count_user + " " + self._code_phone + " " + self._code_citycity)
        return (self.name_state, self._count_user, self. name_statee, self.code_phone, self.code_city, self.country)

    def print_pablic_inf_1(self):
        return self.print_privat_inf()

town = City(
    "Ташкент",
    "Узб",
    "3 000 000",
    "998",
    "01",
    "Узбекистан"
)

# print(homo.print_pablic_inf())
print(homo.print_pablic_inf_1())



