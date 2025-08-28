from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_operation_data import ReqOperationData
from entity.operation_data import OperationData
from service.operation_data import OperationDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Operation Data"])

srv = OperationDataService()


@router.post("/operation_data")
def operation_data(req: Annotated[ReqOperationData, Body(
    example={
        "code": "sh.600000",
        "year": 2018,
        "quarter": 2
    }
)]) -> list[OperationData]:
    try:
        res = srv.query_operation_data(req.code, req.year, req.quarter)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
