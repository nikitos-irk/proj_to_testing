from admin import Admin


def main():
    my_admin = Admin()
    my_admin.create()
    my_customer = my_admin.create_customer()
    my_customer.login(password="123")
    my_machine = my_customer.create_machine()
    my_machine.remove()


if __name__ == "__main__":
    main()
