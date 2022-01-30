import pytest


@pytest.fixture(scope='package')
def create_customer(request, create_admin):
    print(f'{create_admin.name} is here...')
    scope_name = 'PACKAGE'

    def fin():
        print(f'Finish of {scope_name} fixture!')
    request.addfinalizer(fin)

    return create_admin.create_customer()


@pytest.fixture(scope="class")
def create_machine(request, create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    scope_name = 'CLASS'
    vm = create_customer.create_machine()

    def fin():
        print(f'Finish of {scope_name} fixture!')
    request.addfinalizer(fin)

    return vm
