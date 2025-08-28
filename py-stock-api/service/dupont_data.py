import baostock as bs
import pandas as pd

from entity.dupont_data import DupontData
from utilities.query_exception import QueryException


class DupontDataService:

    @classmethod
    def query_dupont_data(cls, code: str, year: int, quarter: int) -> list[DupontData]:
        rs = bs.query_dupont_data(
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
        ks: list[DupontData] = []
        for j in js:
            ks.append(DupontData(**j))
        return ks
