class Oseba:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def izpisi_starost(self):
        print("Starost je: " + str(self.starost))

    def __str__(self):
        return f"{self.ime}"


o1 = Oseba("Janez", 20)

print("Ime: ", o1.ime)

print("Starost: ", o1.starost)

print(o1)

o1.starost = 25

print("Starost: ", o1.starost)


class Sportnik(Oseba):
    pass


s1 = Sportnik("Joze", 37)

s1.izpisi_starost()
