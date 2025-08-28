import baostock as bs
import pandas as pd

from entity.adjust_factor import AdjustFactor
from utilities.query_exception import QueryException

class AdjustFactorService:

    @classmethod
    def query_adjust_factor(cls, code: str, start: str, end: str) -> list[AdjustFactor]:
        rs = bs.query_adjust_factor(
            code=code,
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
        ks: list[AdjustFactor] = []
        for j in js:
            ks.append(AdjustFactor(**j))
        return ks