from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_k_history import ReqKMinute, ReqKDay, ReqKWeek, ReqKMonth
from entity.k_minute import KMinute
from service.k_history import KHistoryService
from utilities.query_exception import QueryException

router = APIRouter(
    prefix="/k",
    tags=["K History"]
)

srv = KHistoryService()

@router.post("/minute")
def k_minute(req: Annotated[ReqKMinute, Body(
    example={
      "code": "sh.600000",
      "start": "2025-07-12",
      "end": "2025-07-17",
      "frequency": "30",
      "adjust_flag": "3"
    }
)]) -> list[KMinute]:
    try:
        res = srv.query_history_k_minute(req.code, req.start.strftime("%Y-%m-%d"), req.end.strftime("%Y-%m-%d"), req.frequency, req.adjust_flag)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)

@router.post("/day")
def k_day(req: Annotated[ReqKDay, Body(
    example={
        "code": "sh.600000",
        "start": "2025-07-12",
        "end": "2025-07-17",
        "adjust_flag": "3"
    }
)]):
    try:
        res = srv.query_history_k_day(req.code, req.start.strftime("%Y-%m-%d"), req.end.strftime("%Y-%m-%d"),
                                         req.adjust_flag)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)

@router.post("/week")
def k_week(req: Annotated[ReqKWeek, Body(
    example={
        "code": "sh.600000",
        "start": "2025-04-12",
        "end": "2025-07-17",
        "adjust_flag": "3"
    }
)]):
    try:
        res = srv.query_history_k_week(req.code, req.start.strftime("%Y-%m-%d"), req.end.strftime("%Y-%m-%d"),
                                      req.adjust_flag)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)

@router.post("/month")
def k_month(req: Annotated[ReqKMonth, Body(
    example={
        "code": "sh.600000",
        "start": "2024-07-12",
        "end": "2025-07-17",
        "adjust_flag": "3"
    }
)]):
    try:
        res = srv.query_history_k_month(req.code, req.start.strftime("%Y-%m-%d"), req.end.strftime("%Y-%m-%d"),
                                      req.adjust_flag)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
