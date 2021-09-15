import uuid
import time


class VirtualMachine:
    def __init__(self):
        self.name = None
        self.created = False
        self.removed = False
        self.active = False

    def create(self):
        print("Virtual machine is starting to be created...")
        if self.created or self.removed:
            raise Exception("Machine is already created/removed!")
        self.name = f"Machine-{str(uuid.uuid4())[:8]}"
        time.sleep(5)
        self.created = True
        self.active = True
        print(f"Virtual machine {self.name} creating finished")
        return True

    def remove(self):
        print(f"Virtual machine {self.name} is starting to be removed...")
        if not self.created or self.removed:
            raise Exception("Machine is not created or already removed!")
        self.removed = True
        self.active = False
        time.sleep(5)
        print("Virtual machine removing finished")
        return True

    def turn_off(self):
        print(f"Virtual machine {self.name} is starting to be off...")
        result = True
        if not self.created or self.removed:
            raise Exception("You can't turn it off")
        if not self.active:
            result = False
        time.sleep(2)
        self.active = False
        print("Virtual machine turning off operation has been finished")
        return result

    def turn_on(self):
        print(f"Virtual machine {self.name} is starting to be on...")
        result = True
        if not self.created or self.removed:
            raise Exception("You can't turn it on")
        if self.active:
            result = False
        time.sleep(2)
        self.active = True
        print("Virtual machine turning on operation has been finished")
        return result

    def restart(self):
        print(f"Virtual machine {self.name} is starting to be restarted...")
        result = True
        if not self.created or self.removed:
            raise Exception("You can't restart")
        if not self.active:
            result = False
        time.sleep(3)
        print("Virtual machine restarting operation has been finished")
        return result
