class card:
   def __init__(self, name, surname, company, job, email):
       self.name = name
       self.surname = surname
       self.company = company
       self.job = job
       self.email = email
   def concacting(self):
       print(f"Kontaktuję się z {self.name} {self.surname}, {self.job} {self.email}")
   def  label_length(self):
       full_name_length = len(self.name) + len(self.surname) + 1
       print(f"Długość imienia i nazwiska dla {self.name} {self.surname} to {full_name_length}") 

class BaseContact(card):
    def __init__(self, name, surname, phone, email):
       self.name = name
       self.surname = surname
       self.email = email
       self.phone = phone
    def concact(self):
        print(f"Wybieram numer {self.phone} i dzwonię {self.name} {self.surname}")

class BusinessContact(card):
    def __init__(self, name, surname, company, job, email, business_phone):
        self.name = name
        self.surname = surname
        self.company = company
        self.job = job
        self.email = email
        self.business_phone = business_phone
    def concact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię {self.name} {self.surname}")    

a = card(name = "Martyna", surname = "Caronia", company = "Vogue", job = "fashion designer", email = "mc@.com")
b = card(name = "Beroo", surname = "Elalfi", company = "Vogue", job = "photographer", email = "be@.com")
c = card(name = "Jowita", surname = "Wojciechowska", company = "TVP", job = "TV reporter", email = "jw@.com")
d = card(name = "Janek", surname = "Leśnik", company = "Thetre", job = "dancer", email = "jl@.com")
e = card(name = "Ewelina", surname = "Turczyńska", company = "louvre", job = "painter", email = "et@.com")

cards = [a,b,c,d,e]


for card in cards:
    card.concacting()
    card.label_length()

def create_contacts(y):
    from faker import Faker
    fake = Faker()

    for x in range(y):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        company = fake.company()
        job = fake.job()
        phone_number = fake.phone_number()

        person = [first_name, last_name, company, job, email, phone_number]
        
        print(person)

create_contacts(5)