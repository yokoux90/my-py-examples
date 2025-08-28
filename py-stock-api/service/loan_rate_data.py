import baostock as bs
import pandas as pd

from entity.loan_rate_data import LoanRateData
from utilities.query_exception import QueryException


class LoanRateDataService:

    @classmethod
    def query_loan_rate_data(cls, start: str, end: str) -> list[LoanRateData]:
        rs = bs.query_loan_rate_data(
            start_date=start,
            end_date=end
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[LoanRateData] = []
        for j in js:
            ks.append(LoanRateData(**j))
        return ks
