
import baostock as bs
from rich.pretty import pprint

from service.loan_rate_data import LoanRateDataService


class TestLoanRateDataService:
    srv: LoanRateDataService

    def setup_class(self):
        bs.login()
        self.srv = LoanRateDataService()

    @classmethod
    def test_query_loan_rate_data(cls):
        rst = cls.srv.query_loan_rate_data(
            start="2015-01-01", end="2017-12-31")
        pprint(rst)
