# test_machine.py

class TestMachine:
    def test_m1(self, machine_restart_class):
        assert machine_restart_class == True

    def test_m2(self, machine_turnoff_class):
        assert machine_turnoff_class["t_off"] == True

    def test_m3(self, machine_turnoff_class):
        assert machine_turnoff_class["act"] == False

    def test_m4(self, machine_turnon_class):
        assert machine_turnon_class["t_on"] == True

    def test_m5(self, machine_turnon_class):
        assert machine_turnon_class["act"] == True

    def test_m6(self, machine_remove_class):
        assert machine_remove_class["rm"] == True

    def test_m7(self, machine_remove_class):
        assert machine_remove_class["act"] == False
