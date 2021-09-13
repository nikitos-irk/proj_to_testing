import pytest
import uuid


INDENTS = {
    "SESSION":  "-" * 15 + ">",
    "MODULE":   "-" * 10 + ">",
    "CLASS":    "-" * 5 + ">",
    "FUNCTION": "->"
}


@pytest.fixture(scope="session")
def fruit_session(request):
    scope_name = "SESSION"
    print(f"{INDENTS[scope_name]}Start of {scope_name} fixture!")

    def fin():
        print(f"{INDENTS[scope_name]}Finish of {scope_name} fixture!")
    request.addfinalizer(fin)

    return str(uuid.uuid4())


@pytest.fixture(scope="module")
def fruit_module(request):
    scope_name = "MODULE"
    print(f"{INDENTS[scope_name]}Start of {scope_name} fixture!")

    def fin():
        print(f"{INDENTS[scope_name]}Finish of {scope_name} fixture!")
    request.addfinalizer(fin)

    return str(uuid.uuid4())


@pytest.fixture(scope="class")
def fruit_class(request):
    scope_name = "CLASS"
    print(f"{INDENTS[scope_name]}Start of {scope_name} fixture!")

    def fin():
        print(f"{INDENTS[scope_name]}Finish of {scope_name} fixture!")

    return str(uuid.uuid4())


@pytest.fixture(scope="function")
def fruit_func(request):
    scope_name = "FUNCTION"
    print(f"{INDENTS[scope_name]}Start of {scope_name} fixture!")

    def fin():
        print(f"{INDENTS[scope_name]}Finish of {scope_name} fixture!")

    return str(uuid.uuid4())
