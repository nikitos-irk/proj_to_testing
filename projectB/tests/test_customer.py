# test_customer.py

class TestCustomer:
    def test_c1(self, customer_scope_session):
        assert customer_scope_session.created == True

    def test_c2(self, customer_scope_module):
        assert customer_scope_module["l_res"] == True

    def test_c3(self, customer_scope_module):
        assert customer_scope_module["ol"] == True

    def test_c4(self, customer_machine_module):
        assert customer_machine_module.created == True

    def test_c5(self, customer_machine_module):
        assert customer_machine_module.active == True

    def test_c6(self, customer_logout_module):
        assert customer_logout_module["l_res"] == True

    def test_c7(self, customer_logout_module):
        assert customer_logout_module["ol"] == False

    def test_c8(self, customer_remove_module):
        assert customer_remove_module == True