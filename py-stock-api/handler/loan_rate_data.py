from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from dto.req_loan_rate_data import ReqLoanRateData
from entity.loan_rate_data import LoanRateData
from service.loan_rate_data import LoanRateDataService
from utilities.query_exception import QueryException

router = APIRouter(tags=["Loan Rate Data"])

srv = LoanRateDataService()


@router.post("/loan_rate_data")
def loan_rate_data(req: Annotated[ReqLoanRateData, Body(
    example={
        "start": "2015-01-01",
        "end": "2017-12-31"
    }
)]) -> list[LoanRateData]:
    try:
        res = srv.query_loan_rate_data(req.start, req.end)
        return res
    except QueryException as e:
        raise HTTPException(status_code=500, detail=e.message)
