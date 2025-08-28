
import baostock as bs
from rich.pretty import pprint

from service.forecast_report import ForecastReportService


class TestForecastReportService:
    srv: ForecastReportService

    def setup_class(self):
        bs.login()
        self.srv = ForecastReportService()

    @classmethod
    def test_query_forecast_report(cls):
        rst = cls.srv.query_forecast_report(
            code="sh.600000", start="2015-01-01", end="2017-12-31")
        pprint(rst)
