# test_admin.py

class TestAdmin:
    def test_1(self, admin_scope_session):
        assert admin_scope_session["result"] == True

    def test_2(self, admin_scope_session):
        assert admin_scope_session["admin"].created == True

