import baostock as bs
import pandas as pd

from entity.forecast_report import ForecastReport
from utilities.query_exception import QueryException


class ForecastReportService:

    @classmethod
    def query_forecast_report(cls, code: str, start: str, end: str) -> list[ForecastReport]:
        rs = bs.query_forecast_report(
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
        ks: list[ForecastReport] = []
        for j in js:
            ks.append(ForecastReport(**j))
        return ks
