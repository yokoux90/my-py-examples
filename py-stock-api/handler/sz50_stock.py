from typing import Annotated

from fastapi import APIRouter, Body, HTTPException


from entity.sz50_stock import SZ50Stock
from service.sz50_stock import SZ50StockService
from utilities.query_exception import QueryException

router = APIRouter(tags=["SZ50 Stock"])

srv = SZ50StockService()


@router.post("/sz50_stock")
def sz50_stock() -> list[SZ50Stock]:
    try:
        res = srv.query_sz50_stocks()
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
