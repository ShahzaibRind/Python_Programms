class Dad():
    basketball = 2

class Son(Dad):
    dance = 4
    def isDance(self):
        return f"Sunny Dance for {self.dance} no of times.."

class Grandson(Son):
    dance = 9
    score =100
    def isDance(self):
        return f"Grancy Dance for {self.dance} no of times " \
    f"And Also scored {self.score} in every match"


Daddy = Dad()
Sunny = Son()
Grancy = Grandson()

print(Grancy.isDance())