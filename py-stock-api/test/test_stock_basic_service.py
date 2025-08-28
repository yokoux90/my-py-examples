
import baostock as bs
from rich.pretty import pprint

from service.stock_basic import StockBasicService


class TestStockBasicService:
    srv: StockBasicService

    def setup_class(self):
        bs.login()
        self.srv = StockBasicService()

    @classmethod
    def test_query_stock_basic(cls):
        rst = cls.srv.query_stock_basic(code="sh.600000")
        pprint(rst)
