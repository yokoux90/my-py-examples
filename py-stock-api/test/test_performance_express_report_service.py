
import baostock as bs
from rich.pretty import pprint

from service.performance_express_report import PerformanceExpressReportService


class TestPerformanceExpressReportFactorService:
    srv: PerformanceExpressReportService

    def setup_class(self):
        bs.login()
        self.srv = PerformanceExpressReportService()

    @classmethod
    def test_query_performance_express_report(cls):
        rst = cls.srv.query_performance_express_report(
            code="sh.600000", start="2015-01-01", end="2017-12-31")
        pprint(rst)
