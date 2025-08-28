from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_forecast_report import ReqForecastReport
from entity.forecast_report import ForecastReport
from service.forecast_report import ForecastReportService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Forecast Report"])

srv = ForecastReportService()


@router.post("/forecast_report")
def forecast_report(req: Annotated[ReqForecastReport, Body(
    example={
        "code": "sh.600000",
        "start": "2015-01-01",
        "end": "2017-12-31"
    }
)]) -> list[ForecastReport]:
    try:
        res = srv.query_forecast_report(req.code, req.start, req.end)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
