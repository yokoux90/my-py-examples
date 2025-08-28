
import baostock as bs
from rich.pretty import pprint

from service.deposit_rate_data import DepositRateDataService


class TestDepositRateDataService:
    srv: DepositRateDataService

    def setup_class(self):
        bs.login()
        self.srv = DepositRateDataService()

    @classmethod
    def test_query_deposit_rate_data(cls):
        rst = cls.srv.query_deposit_rate_data(
            start="2015-01-01", end="2017-12-31")
        pprint(rst)
