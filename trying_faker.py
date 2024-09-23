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