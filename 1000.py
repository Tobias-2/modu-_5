import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the difference
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper


@time_it
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

create_contacts(1000)