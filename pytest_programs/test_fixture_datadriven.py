import pytest
from pytest_programs.BaseClass import BaseClass


@pytest.mark.usefixtures("data_example")
class TestExampleDatadriven(BaseClass):

    def test_edit_profile(self, data_example):

        log = self.get_logger()
        log.info(data_example)
        log.info(data_example[0])
        log.info(data_example[1])
        #print(data_example)





