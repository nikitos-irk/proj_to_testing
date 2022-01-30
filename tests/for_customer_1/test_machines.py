import pytest


class TestMachineA:
    @pytest.mark.prb
    def test_create_machine_1(self, create_admin, create_customer, create_machine):
        print(f'[{create_admin.name}] -> [{create_customer.name}] -> [{create_machine.name}]')
        assert create_machine.created is True
        assert create_machine.active is False

    @pytest.mark.prb
    def test_turnoff_machine_1(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        res = create_machine.turn_off()
        assert res is False

    @pytest.mark.prb
    def test_turnon_machine_1(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        res = create_machine.turn_on()
        assert res is True

    @pytest.mark.prb
    def test_turnon_2_machine_1(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        res = create_machine.turn_on()
        assert res is False

    @pytest.mark.prb
    def test_turnoff_2_machine_1(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        res = create_machine.turn_off()
        assert res is True
        assert create_machine.active is False

    @pytest.mark.prb
    def test_remove_machine_1(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        res = create_machine.remove()
        assert res is True
        assert create_machine.removed is True
        assert create_machine.created is False

    @pytest.mark.prb
    def test_remove_2_machine_1(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        with pytest.raises(Exception):
            create_machine.remove()


class TestMachineB:
    def test_restart_machine_2(self, create_admin, create_customer, create_machine):
        print(f'[{create_admin.name}] -> [{create_customer.name}] -> [{create_machine.name}]')
        res = create_machine.restart()
        assert res is False

    def test_restart_2_machine_2(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        create_machine.turn_on()
        res = create_machine.restart()
        assert res is True

    def test_restart_3_machine_2(self, create_customer, create_machine):
        print(f'[{create_customer.name}] -> [{create_machine.name}]')
        create_machine.remove()
        with pytest.raises(Exception):
            create_machine.restart()
