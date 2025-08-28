from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_dupont_data import ReqDupontData
from entity.dupont_data import DupontData
from service.dupont_data import DupontDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Dupont Data"])

srv = DupontDataService()


@router.post("/dupont_data")
def dupont_data(req: Annotated[ReqDupontData, Body(
    example={
        "code": "sh.600000",
        "year": 2018,
        "quarter": 2
    }
)]) -> list[DupontData]:
    try:
        res = srv.query_dupont_data(req.code, req.year, req.quarter)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
