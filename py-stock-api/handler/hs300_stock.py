from typing import Annotated

from fastapi import APIRouter, Body, HTTPException


from entity.hs300_stock import HS300Stock
from service.hs300_stock import HS300StockService
from utilities.query_exception import QueryException

router = APIRouter(tags=["HS300 Stock"])

srv = HS300StockService()


@router.post("/hs300_stock")
def hs300_stock() -> list[HS300Stock]:
    try:
        res = srv.query_hs300_stocks()
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
