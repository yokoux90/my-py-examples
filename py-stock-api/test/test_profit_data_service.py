import baostock as bs
from rich.pretty import pprint

from service.profit_data import ProfitDataService


class TestProfitDataService:
    srv: ProfitDataService

    def setup_class(self):
        bs.login()
        self.srv = ProfitDataService()

    @classmethod
    def test_query_profit_data(cls):
        rst = cls.srv.query_profit_data(code="sh.600000", year=2018, quarter=2)
        pprint(rst)
