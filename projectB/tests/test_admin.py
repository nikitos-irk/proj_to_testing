import pytest


@pytest.mark.prb
def test_admin(create_admin):
    create_admin.create()
    assert create_admin.created is True
    assert create_admin.name[:5] == 'Admin'
