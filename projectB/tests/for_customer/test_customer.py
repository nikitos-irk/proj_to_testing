import pytest


@pytest.mark.prb
def test_customer(create_admin, create_customer):
    print(f'...and {create_customer.name} too')
    assert create_customer.created is True
    assert create_customer.name[:8] == 'Customer'
    assert create_customer.machines == []
    assert len(create_admin.customers) == 1


@pytest.mark.prb
def test_customer_2(create_admin, create_customer):
    print(f'...and {create_customer.name} too')
    assert create_customer.created is True
    assert create_customer.name[:8] == 'Customer'
    assert create_customer.machines == []
    assert len(create_admin.customers) == 2
