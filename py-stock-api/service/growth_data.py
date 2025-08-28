import baostock as bs
import pandas as pd

from entity.growth_data import GrowthData
from utilities.query_exception import QueryException

class GrowthDataService:

    @classmethod
    def query_growth_data(cls, code: str, year: int, quarter: int) -> list[GrowthData]:
        rs = bs.query_growth_data(
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
        ks: list[GrowthData] = []
        for j in js:
            ks.append(GrowthData(**j))
        return ks