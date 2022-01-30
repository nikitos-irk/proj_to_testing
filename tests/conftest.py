import pytest
from projectB.admin import Admin
from projectB.customer import Customer


@pytest.fixture(scope='session')
def create_admin(request):
    scope_name = 'SESSION'
    adm = Admin()
    adm.create()

    def fin():
        print(f'Finish of {scope_name} fixture!')
    request.addfinalizer(fin)

    return adm


@pytest.fixture(scope='session')
def wrong_customer(request):
    scope_name = 'SESSION'

    def fin():
        print(f'Finish of {scope_name} fixture!')
    request.addfinalizer(fin)

    return Customer()
