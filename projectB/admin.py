import uuid
import time

from customer import Customer


class Admin:
    def __init__(self):
        self.name = None
        self.created = False
        self.customers = []

    def create(self):
        print("Admin creating starts...")
        self.name = f"Admin-{str(uuid.uuid4())[:8]}"
        self.created = True
        time.sleep(5)
        print(f"Admin {self.name} creating ends")
        return True

    def create_customer(self):
        print("Admin is going to create customer...")
        new_customer = Customer()
        new_customer.create()
        self.customers.append(new_customer)
        print("Admin finished to create customer")
        return new_customer
