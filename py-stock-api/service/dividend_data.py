import baostock as bs
import pandas as pd

from constant.year_type import YearType
from entity.dividend_data import DividendData
from utilities.query_exception import QueryException


class DividendDataService:

    @classmethod
    def query_dividend_data(cls, code: str, year: str, yt: YearType) -> list[DividendData]:
        rs = bs.query_dividend_data(
            code=code,
            year=year,
            yearType=str(yt)
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[DividendData] = []
        for j in js:
            ks.append(DividendData(**j))
        return ks
