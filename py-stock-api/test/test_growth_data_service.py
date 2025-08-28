import baostock as bs
from rich.pretty import pprint

from service.growth_data import GrowthDataService


class TestGrowthDataService:
    srv: GrowthDataService

    def setup_class(self):
        bs.login()
        self.srv = GrowthDataService()

    @classmethod
    def test_query_growth_data(cls):
        rst = cls.srv.query_growth_data(code="sh.600000", year=2018, quarter=2)
        pprint(rst)
