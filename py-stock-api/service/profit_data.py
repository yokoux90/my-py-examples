import baostock as bs
import pandas as pd

from entity.profit_data import ProfitData
from utilities.query_exception import QueryException

class ProfitDataService:

    @classmethod
    def query_profit_data(cls, code: str, year: int, quarter: int) -> list[ProfitData]:
        rs = bs.query_profit_data(
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
        ks: list[ProfitData] = []
        for j in js:
            ks.append(ProfitData(**j))
        return ks