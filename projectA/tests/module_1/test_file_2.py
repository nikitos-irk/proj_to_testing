import pytest
import uuid


class TestB:
    def test_1(self, fruit_session, fruit_module, fruit_class, fruit_func):
        print(f"Session: {fruit_session}")
        print(f"Module: {fruit_module}")
        print(f"CLASS: {fruit_class}")
        print(f"FUNC: {fruit_func}")
        assert True

    def test_2(self, fruit_session, fruit_module, fruit_class, fruit_func):
        print(f"Session: {fruit_session}")
        print(f"Module: {fruit_module}")
        print(f"CLASS: {fruit_class}")
        print(f"FUNC: {fruit_func}")
        assert True

    def test_3(self, fruit_session, fruit_module, fruit_class, fruit_func):
        print(f"Session: {fruit_session}")
        print(f"Module: {fruit_module}")
        print(f"CLASS: {fruit_class}")
        print(f"FUNC: {fruit_func}")
        assert True
