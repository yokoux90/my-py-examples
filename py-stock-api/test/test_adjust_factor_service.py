
import baostock as bs
from rich.pretty import pprint

from service.adjust_factor import AdjustFactorService


class TestAdjustFactorService:
    srv: AdjustFactorService

    def setup_class(self):
        bs.login()
        self.srv = AdjustFactorService()

    @classmethod
    def test_query_adjust_factor(cls):
        rst = cls.srv.query_adjust_factor(code="sh.600000", start="2015-01-01", end="2017-12-31")
        pprint(rst)
