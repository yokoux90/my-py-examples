from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_money_supply_data_year import ReqMoneySupplyDataYear
from entity.money_supply_data_year import MoneySupplyDataYear
from service.money_supply_data_year import MoneySupplyDataYearService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Money Supply Data Year"])

srv = MoneySupplyDataYearService()


@router.post("/money_supply_data_year")
def money_supply_data_year(req: Annotated[ReqMoneySupplyDataYear, Body(
    example={
        "start_date": "2015-01-01",
        "end_date": "2017-12-31"
    }
)]) -> list[MoneySupplyDataYear]:
    try:
        res = srv.query_money_supply_data_year(req.start_date, req.end_date)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
