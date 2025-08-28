import baostock as bs
from rich.pretty import pprint

from service.cash_flow_data import CashFlowDataService


class TestCashFlowDataService:
    srv: CashFlowDataService

    def setup_class(self):
        bs.login()
        self.srv = CashFlowDataService()

    @classmethod
    def test_query_cash_flow_data(cls):
        rst = cls.srv.query_cash_flow_data(
            code="sh.600000", year=2018, quarter=2)
        pprint(rst)
