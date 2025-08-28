import baostock as bs
from rich.pretty import pprint

from service.balance_data import BalanceDataService


class TestBalanceDataService:
    srv: BalanceDataService

    def setup_class(self):
        bs.login()
        self.srv = BalanceDataService()

    @classmethod
    def test_query_balance_data(cls):
        rst = cls.srv.query_balance_data(
            code="sh.600000", year=2018, quarter=2)
        pprint(rst)
