class ComputerScience():
    subjects = 5
    def it(self):
        return f"'Computer Science:' There is Only {self.subjects} Subjects."
class InfoTech(ComputerScience):
    lab = 9
    def it(self):
        return f"'Information Technology: ' there is {self.lab} labs and {self.subjects} Subjects"

class SoftwareEngeneering(InfoTech):
    sports = 7
    def it(self):
        return f"'Software Engineering: ' there are {self.subjects} Subjects, {self.lab} Labs and Also {self.sports} days Sports in month"

cs = ComputerScience()
it = InfoTech()
se = SoftwareEngeneering()

print(cs.it())
print(it.it())
print(se.it())