import pytest
from projectB.admin import Admin


@pytest.fixture(scope='session')
def create_admin():
    return Admin()
