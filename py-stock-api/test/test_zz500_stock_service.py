
import baostock as bs
from rich.pretty import pprint

from service.zz500_stock import ZZ500StockService


class TestZZ500StockService:
    srv: ZZ500StockService

    def setup_class(self):
        bs.login()
        self.srv = ZZ500StockService()

    @classmethod
    def query_sz50_stocks(cls):
        rst = cls.srv.query_zz500_stocks()
        pprint(rst)
