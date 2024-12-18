import pytest


@pytest.fixture(scope="class")
def setup():
    print("I am printing from the confest, I print first")


@pytest.fixture()
def data_example():
    print("Enter all the details: ")
    return ["Shruti", "Python", 37, "shrutib@gmail.com"]


@pytest.fixture(params=[("Shruti", "BE", 40), ("B", 66, "SZ"), (25, 37, "shrutib@gmail.com")])
def data_param(request):
    return request.param
