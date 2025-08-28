import baostock as bs
from rich.pretty import pprint

from service.dupont_data import DupontDataService


class TestDupontDataService:
    srv: DupontDataService

    def setup_class(self):
        bs.login()
        self.srv = DupontDataService()

    @classmethod
    def test_query_dupont_data(cls):
        rst = cls.srv.query_dupont_data(
            code="sh.600000", year=2018, quarter=2)
        pprint(rst)
