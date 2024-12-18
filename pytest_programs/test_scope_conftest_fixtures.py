import pytest



@pytest.mark.usefixtures("setup")
class TestExample:

    def test_demo1(self):
        print("I printed from demo1 method")

    def test_demo2(self):
        print("I printed from demo2 method")

    def test_demo3(self):
        print("I printed from demo3 method")
