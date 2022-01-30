import pytest


@pytest.mark.prb
def test_customer(create_admin, create_customer):
    print(f'...and [{create_customer.name}] too')
    assert create_customer.created is True
    assert create_customer.name[:8] == 'Customer'
    assert create_customer.machines == []
    assert len(create_admin.customers) == 1


@pytest.mark.prb
def test_customer_login_1(create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    res = create_customer.login("")
    assert res is False
    assert create_customer.online is False


@pytest.mark.prb
def test_wrong_create_machine_1(wrong_customer):
    print(f'Thief [{wrong_customer.name}]')
    with pytest.raises(Exception):
        wrong_customer.create_machine()


@pytest.mark.prb
def test_customer_create_machine_1(create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    with pytest.raises(Exception):
        create_customer.create_machine()


@pytest.mark.prb
def test_customer_login_2(create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    res = create_customer.login("123")
    assert res is True
    assert create_customer.online is True
