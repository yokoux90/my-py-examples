import baostock as bs
from rich.pretty import pprint
from service.k_history import KHistoryService


class TestKHistoryService:
    srv: KHistoryService

    def setup_class(self):
        bs.login()
        self.srv = KHistoryService()

    def test_query_minute(self):
        rst = self.srv.query_history_k_minute(code="sh.600000",
                                              start="2025-07-12",
                                              end="2025-07-17",
                                              frequency="30",
                                              adjust_flag="3"
                                              )
        pprint(rst)

    def test_query_day(self):
        rst = self.srv.query_history_k_day(code="sh.600000",
                                              start="2025-07-12",
                                              end="2025-07-17",
                                              adjust_flag="3"
                                              )
        pprint(rst)

    def test_query_week(self):
        rst = self.srv.query_history_k_week(code="sh.600000",
                                              start="2024-07-12",
                                              end="2025-01-17",
                                              adjust_flag="3"
                                              )
        pprint(rst)

    def test_query_month(self):
        rst = self.srv.query_history_k_month(code="sh.600000",
                                              start="2024-07-12",
                                              end="2025-07-17",
                                              adjust_flag="3"
                                              )
        pprint(rst)