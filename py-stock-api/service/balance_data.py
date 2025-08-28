import baostock as bs
import pandas as pd

from entity.balance_data import BalanceData
from utilities.query_exception import QueryException


class BalanceDataService:

    @classmethod
    def query_balance_data(cls, code: str, year: int, quarter: int) -> list[BalanceData]:
        rs = bs.query_balance_data(
            code=code,
            year=year,
            quarter=quarter
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[BalanceData] = []
        for j in js:
            ks.append(BalanceData(**j))
        return ks
