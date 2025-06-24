# 1️⃣ SINGLE INHERITANCE
class Father:
    def bike(self):
        print("Father rides a Royal Enfield")

class Son(Father):
    def cycle(self):
        print("Son rides a bicycle")

print("---- Single Inheritance ----")
s1 = Son()
s1.bike()
s1.cycle()


# 2️⃣ MULTIPLE INHERITANCE
class Father:
    def job(self):
        print("Father is an engineer")

class Mother:
    def hobby(self):
        print("Mother loves painting")

class Son(Father, Mother):
    def play(self):
        print("Son plays football")

print("\n---- Multiple Inheritance ----")
s2 = Son()
s2.job()
s2.hobby()
s2.play()


# 3️⃣ MULTILEVEL INHERITANCE
class Human:
    def species(self):
        print("I am a human")

class Male(Human):
    def gender(self):
        print("Gender: Male")

class Arun(Male):
    def name(self):
        print("My name is Arun")

print("\n---- Multilevel Inheritance ----")
a = Arun()
a.species()
a.gender()
a.name()


# 4️⃣ HIERARCHICAL INHERITANCE
class Father:
    def property(self):
        print("Father owns 10 acres of land")

class Son(Father):
    def bike(self):
        print("Son has a bike")

class Daughter(Father):
    def laptop(self):
        print("Daughter has a MacBook")

class YoungerDaughter(Father):
    def tablet(self):
        print("Younger Daughter has a tablet")

print("\n---- Hierarchical Inheritance ----")
s3 = Son()
d = Daughter()
y = YoungerDaughter()

s3.property()
s3.bike()

d.property()
d.laptop()

y.property()
y.tablet()


# 5️⃣ HYBRID INHERITANCE (Multilevel + Multiple)
class Grandfather:
    def wisdom(self):
        print("Grandfather shares wisdom")

class Father(Grandfather):
    def job(self):
        print("Father is a doctor")

class Mother:
    def cook(self):
        print("Mother cooks well")

class Son(Father, Mother):  # Hybrid: multilevel + multiple
    def study(self):
        print("Son is a student")

print("\n---- Hybrid Inheritance ----")
s4 = Son()
s4.wisdom()
s4.job()
s4.cook()
s4.study()
