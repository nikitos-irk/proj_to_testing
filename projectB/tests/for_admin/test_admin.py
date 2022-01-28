import pytest


@pytest.mark.prb
def test_admin(create_admin):
    print(f'{create_admin.name} has been created...')
    assert create_admin.created is True
    assert create_admin.name[:5] == 'Admin'
    assert create_admin.customers == []
