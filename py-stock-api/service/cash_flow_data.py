import baostock as bs
import pandas as pd

from entity.cash_flow_data import CashFlowData
from utilities.query_exception import QueryException


class CashFlowDataService:

    @classmethod
    def query_cash_flow_data(cls, code: str, year: int, quarter: int) -> list[CashFlowData]:
        rs = bs.query_cash_flow_data(
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
        ks: list[CashFlowData] = []
        for j in js:
            ks.append(CashFlowData(**j))
        return ks
