from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_stock_basic import ReqStockBasic
from entity.stock_basic import StockBasic
from service.stock_basic import StockBasicService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Stock Basic"])

srv = StockBasicService()


@router.post("/stock_basic")
def stock_basic(req: Annotated[ReqStockBasic, Body(
    example={
        "code": "sh.600000"
    }
)]) -> list[StockBasic]:
    try:
        res = srv.query_stock_basic(req.code)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
