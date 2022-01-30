import pytest


@pytest.mark.prb
def test_customer_2(create_admin, create_customer):
    print(f'...and [{create_customer.name}] too')
    assert create_customer.created is True
    assert create_customer.name[:8] == 'Customer'
    assert create_customer.machines == []
    assert len(create_admin.customers) == 2


@pytest.mark.prb
def test_wrong_logout(wrong_customer):
    print(f'Thief [{wrong_customer.name}]')
    with pytest.raises(Exception):
        wrong_customer.logout()


@pytest.mark.prb
def test_customer_2_logout(create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    with pytest.raises(Exception):
        create_customer.logout()


@pytest.mark.prb
def test_wrong_remove(wrong_customer):
    print(f'Thief [{wrong_customer.name}]')
    with pytest.raises(Exception):
        wrong_customer.remove()


@pytest.mark.prb
def test_customer_2_remove(create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    create_customer.login("123")
    with pytest.raises(Exception):
        create_customer.remove()


@pytest.mark.prb
def test_customer_2_logout_2(create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    res = create_customer.logout()
    assert res is True
    assert create_customer.online is False


@pytest.mark.prb
def test_customer_2_remove_2(create_admin, create_customer):
    print(f'[{create_admin.name}] -> [{create_customer.name}]')
    res = create_customer.remove()
    assert res is True
    assert create_customer.created is False
