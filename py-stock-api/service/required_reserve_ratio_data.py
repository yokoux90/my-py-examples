import baostock as bs
import pandas as pd

from entity.required_reserve_ratio_data import RequiredReserveRatioData
from utilities.query_exception import QueryException


class RequiredReserveRatioDataService:

    @classmethod
    def query_required_reserve_ratio_data(cls, start: str, end: str, yt: str = "0") -> list[RequiredReserveRatioData]:
        rs = bs.query_required_reserve_ratio_data(
            start_date=start,
            end_date=end,
            yearType=yt
        )
        if rs.error_code != '0':
            raise QueryException(rs.error_code, rs.error_message)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        js = result.to_dict(orient='records')
        ks: list[RequiredReserveRatioData] = []
        for j in js:
            ks.append(RequiredReserveRatioData(**j))
        return ks
