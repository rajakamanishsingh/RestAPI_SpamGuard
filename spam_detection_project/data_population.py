from .models import User,Contact
from django.utils.crypto import get_random_string
from faker import Faker
import random
import string

fake = Faker()

def gen_users(count):
    users = []
    for _ in range(count):
        name = fake.name()
        phone_number = fake.phone_number()
        email = fake.email()
        password = get_random_string(32)
        user = User(name=name, phone_number=phone_number, email=email, password=password)
        users.append(user)
    User.objects.bulk_create(users)

def gen_contacts(user, count):
    contacts = []
    for _ in range(count):
        name = fake.name()
        phone_number = fake.phone_number()
        contact = Contact(user=user, name=name, phone_number=phone_number)
        contacts.append(contact)
    Contact.objects.bulk_create(contacts)

if __name__ == '__main__':
    gen_users(100)
    users = User.objects.all()
    for user in users:
        gen_contacts(user, random.randint(0, 10))