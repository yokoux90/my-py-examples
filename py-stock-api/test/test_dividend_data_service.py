import baostock as bs
from service.dividend_data import DividendDataService
from rich.pretty import pprint

class TestDividendDataService:
    srv: DividendDataService

    def setup_class(self):
        bs.login()
        self.srv = DividendDataService()

    @classmethod
    def test_query_dividend_data(cls):
        rst = cls.srv.query_dividend_data(code="sh.601398", year="2018", yt="report")
        pprint(rst)