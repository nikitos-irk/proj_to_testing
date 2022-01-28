import pytest
from projectB.admin import Admin


@pytest.fixture(scope='session')
def create_admin():
    adm = Admin()
    adm.create()
    return adm

@pytest.fixture(scope='class')
def create_customer(create_admin):
    print(f'{create_admin.name} is here...')
    return create_admin.create_customer()
