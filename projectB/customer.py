import uuid
import time

from projectB.machine import VirtualMachine


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
        time.sleep(2)
        print("Customer creating finished")
        return True

    def remove(self):
        print("Customer removing...")
        if not self.created:
            raise Exception("Can't remove non-existing customer")
        if self.online:
            raise Exception("Can't remove if customer is online")
        else:
            time.sleep(1)
            print("Customer removing finished")
            self.created = False

        return True

    def login(self, password):
        print("Customer loggin in...")
        result = False

        if self.online:
            print("Customer is already online")
        elif not self.created:
            raise Exception("Impossible to login if customer was not created!")
        elif password != "123":
            print("Wrong login/password")
        else:
            self.online = True
            result = True
            time.sleep(3)
            print("Customer loggin in finished...")

        return result

    def logout(self):
        print("Customer log out...")

        if not self.created:
            raise Exception(
                "Impossible to logout if a customer was not created!")
        if not self.online:
            raise Exception(
                "Impossible to logout if a customer was not logged in!")
        else:
            self.online = False
            time.sleep(1)
            print("Customer logout finished...")
        return True

    def create_machine(self):
        print("Customer is going to create a machine...")
        if not self.created:
            raise Exception("Customer does not exist!")
        if not self.online:
            raise Exception("Customer is off")
        machine = VirtualMachine()
        machine.create()
        self.machines.append(machine)
        print("Customer finished creating a machine")
        return machine
