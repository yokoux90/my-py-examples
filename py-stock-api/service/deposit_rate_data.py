import baostock as bs
import pandas as pd

from entity.deposit_rate_data import DepositRateData
from utilities.query_exception import QueryException


class DepositRateDataService:

    @classmethod
    def query_deposit_rate_data(cls, start: str, end: str) -> list[DepositRateData]:
        rs = bs.query_deposit_rate_data(
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
        ks: list[DepositRateData] = []
        for j in js:
            ks.append(DepositRateData(**j))
        return ks
