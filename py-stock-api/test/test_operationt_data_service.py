import baostock as bs
from rich.pretty import pprint

from service.operation_data import OperationDataService


class TestOperationDataService:
    srv: OperationDataService

    def setup_class(self):
        bs.login()
        self.srv = OperationDataService()

    @classmethod
    def test_query_operation_data(cls):
        rst = cls.srv.query_operation_data(code="sh.600000", year=2018, quarter=2)
        pprint(rst)
