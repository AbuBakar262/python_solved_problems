class Pakistan():
    def capital(self):
        print("Islamabad is the Capital of Pakistan.")

    def language(self):
        print("Urdu is most widely spoken language of Pakistan.")

    def type(self):
        print("Pakistan is a developing country.")


class USA():
    def capital(self):
        print("Washington D.C is the Capital of USA.")

    def language(self):
        print("English is most widely spoken language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_pak = Pakistan()
obj_usa = USA()

for data in (obj_pak, obj_usa):
    data.capital()
    data.language()
    data.type()
    print("")