
import baostock as bs
from rich.pretty import pprint

from service.money_supply_data_month import MoneySupplyDataMonthService


class TestMoneySupplyDataMonthService:
    srv: MoneySupplyDataMonthService

    def setup_class(self):
        bs.login()
        self.srv = MoneySupplyDataMonthService()

    @classmethod
    def test_query_money_supply_data_month(cls):
        rst = cls.srv.query_money_supply_data_month(
            start="2015-01-01", end="2017-12-31")
        pprint(rst)
