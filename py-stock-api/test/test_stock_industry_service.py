
import baostock as bs
from rich.pretty import pprint

from service.stock_industry import StockIndustryService


class TestStockIndustryService:
    srv: StockIndustryService

    def setup_class(self):
        bs.login()
        self.srv = StockIndustryService()

    @classmethod
    def test_query_stock_industry(cls):
        rst = cls.srv.query_stock_industry()
        pprint(rst)
