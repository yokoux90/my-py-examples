from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_performance_express_report import ReqPerformanceExpressReport
from entity.performance_express_report import PerformanceExpressReport
from service.performance_express_report import PerformanceExpressReportService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Performance Express Report"])

srv = PerformanceExpressReportService()


@router.post("/performance_express_report")
def performance_express_report(req: Annotated[ReqPerformanceExpressReport, Body(
    example={
        "code": "sh.600000",
        "start": "2015-01-01",
        "end": "2017-12-31"
    }
)]) -> list[PerformanceExpressReport]:
    try:
        res = srv.query_performance_express_report(
            req.code, req.start, req.end)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
