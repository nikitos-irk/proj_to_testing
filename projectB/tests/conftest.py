# conftest.py

import pytest
import sys
sys.path.append('C:/temp/py/testproj/projectB')
import admin


@pytest.fixture(scope="session")
def admin_scope_session():
    adm = admin.Admin()
    creating_result = adm.create()
    return {"result": creating_result, "admin": adm}


@pytest.fixture(scope="session")
def customer_scope_session(admin_scope_session):
    customer_result = admin_scope_session["admin"].create_customer()
    return customer_result


@pytest.fixture(scope="package")
def customer_scope_module(customer_scope_session):
    login_result = customer_scope_session.login(password="123")
    online = customer_scope_session.online
    return {"l_res": login_result, "ol": online}


@pytest.fixture(scope="package")
def customer_machine_module(customer_scope_session):
    machine_result = customer_scope_session.create_machine()
    return machine_result


@pytest.fixture(scope="class")
def machine_restart_class(customer_machine_module):
    restart_result = customer_machine_module.restart()
    return restart_result


@pytest.fixture(scope="class")
def machine_turnoff_class(customer_machine_module):
    turnoff_result = customer_machine_module.turn_off()
    active = customer_machine_module.active
    return {"t_off": turnoff_result, "act": active}


@pytest.fixture(scope="class")
def machine_turnon_class(customer_machine_module):
    turnon_result = customer_machine_module.turn_on()
    active = customer_machine_module.active
    return {"t_off": turnon_result, "act": active}


@pytest.fixture(scope="class")
def machine_turnon_class(customer_machine_module):
    turnon_result = customer_machine_module.turn_on()
    active = customer_machine_module.active
    return {"t_on": turnon_result, "act": active}


@pytest.fixture(scope="class")
def machine_remove_class(customer_machine_module):
    remove_result = customer_machine_module.remove()
    active = customer_machine_module.active
    return {"rm": remove_result, "act": active}


@pytest.fixture(scope="package")
def customer_logout_module(customer_scope_session):
    logout_result = customer_scope_session.logout()
    offline = customer_scope_session.online
    return {"l_res": logout_result, "ol": offline}

@pytest.fixture(scope="package")
def customer_remove_module(customer_scope_session):
    remove_result = customer_scope_session.remove()
    return remove_result
