import uuid
import time

from machine import VirtualMachine


class Customer:
    def __init__(self):
        self.name = None
        self.created = False
        self.online = False
        self.machines = []

    def create(self):
        print("Customer creating...")
        self.name = f"Customer-{str(uuid.uuid4())[:8]}"
        self.created = True
        time.sleep(5)
        print(f"Customer {self.name} creating finished")
        return True

    def remove(self):
        print(f"Customer {self.name} removing...")
        result = True
        if not self.created:
            raise Exception("Can't remove non-existing customer")
        if self.online:
            result = False
        time.sleep(1)
        print("Customer removing finished")
        return result

    def login(self, password):
        print(f"Customer {self.name}  loggin in...")
        result = True
        if password != "123":
            result = False
        if not self.created:
            raise Exception("Impossible to login if customer was not created!")

        if self.online:
            print("Customer is already online")
            result = False

        self.online = True
        time.sleep(3)
        print("Customer loggin in finished...")
        return result

    def logout(self):
        print(f"Customer {self.name} log out...")
        result = True

        if not self.created:
            raise Exception(
                "Impossible to logout if customer was not created!")
        if not self.online:
            result = False
        self.online = False
        time.sleep(1)
        print("Customer logout finished...")
        return result

    def create_machine(self):
        print(f"Customer {self.name} is going to create a machine...")
        if not self.created:
            raise Exception("Customer does not exist!")
        if not self.online:
            raise Exception("Customer is off")
        machine = VirtualMachine()
        machine.create()
        self.machines.append(machine)
        print("Customer finished creating a machine")
        return machine
