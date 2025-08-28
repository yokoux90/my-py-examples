
import baostock as bs
from rich.pretty import pprint

from service.sz50_stock import SZ50StockService


class TestSZ50StockService:
    srv: SZ50StockService

    def setup_class(self):
        bs.login()
        self.srv = SZ50StockService()

    @classmethod
    def query_sz50_stocks(cls):
        rst = cls.srv.query_sz50_stocks()
        pprint(rst)
