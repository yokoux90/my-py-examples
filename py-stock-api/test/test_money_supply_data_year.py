
import baostock as bs
from rich.pretty import pprint

from service.money_supply_data_year import MoneySupplyDataYearService


class TestMoneySupplyDataYearService:
    srv: MoneySupplyDataYearService

    def setup_class(self):
        bs.login()
        self.srv = MoneySupplyDataYearService()

    @classmethod
    def test_query_money_supply_data_year(cls):
        rst = cls.srv.query_money_supply_data_year(
            start="2015-01-01", end="2017-12-31")
        pprint(rst)
