import pytest


@pytest.fixture(scope='package')
def create_customer(request, create_admin):
    print(f'{create_admin.name} is here...')

    scope_name = 'PACKAGE'

    def fin():
        print(f'Finish of {scope_name} fixture!')
    request.addfinalizer(fin)

    return create_admin.create_customer()
