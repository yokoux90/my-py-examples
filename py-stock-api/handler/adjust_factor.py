from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_adjust_factor import ReqAdjustFactor
from entity.adjust_factor import AdjustFactor
from service.adjust_factor import AdjustFactorService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Adjust Factor"])

srv = AdjustFactorService()


@router.post("/adjust_factor")
def adjust_factor(req: Annotated[ReqAdjustFactor, Body(
    example={
        "code": "sh.600000",
        "start": "2015-01-01",
        "end": "2017-12-31"
    }
)]) -> list[AdjustFactor]:
    try:
        res = srv.query_adjust_factor(req.code, req.start, req.end)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
