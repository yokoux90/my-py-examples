
import baostock as bs
from rich.pretty import pprint

from service.hs300_stock import HS300StockService


class TestHS300StockService:
    srv: HS300StockService

    def setup_class(self):
        bs.login()
        self.srv = HS300StockService()

    @classmethod
    def query_sz50_stocks(cls):
        rst = cls.srv.query_hs300_stocks()
        pprint(rst)
