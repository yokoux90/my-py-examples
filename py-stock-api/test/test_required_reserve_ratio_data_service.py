
import baostock as bs
from rich.pretty import pprint

from service.required_reserve_ratio_data import RequiredReserveRatioDataService


class TestRequiredReserveRatioService:
    srv: RequiredReserveRatioDataService

    def setup_class(self):
        bs.login()
        self.srv = RequiredReserveRatioDataService()

    @classmethod
    def test_query_required_reserve_ratio_data(cls):
        rst = cls.srv.query_required_reserve_ratio_data(
            start="2015-01-01", end="2017-12-31")
        pprint(rst)
