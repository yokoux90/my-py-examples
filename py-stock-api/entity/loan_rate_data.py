from pydantic import BaseModel, Field


class LoanRateData(BaseModel):
    """
    贷款利率
    """
    pubDate: str | None = Field(default=None, title="发布日期")
    loanRate6Month: str | None = Field(default=None, title="6个月贷款利率")
    loanRate6MonthTo1Year: str | None = Field(default=None, title="6个月至1年贷款利率")
    loanRate1YearTo3Year: str | None = Field(default=None, title="1年至3年贷款利率")
    loanRate3YearTo5Year: str | None = Field(default=None, title="3年至5年贷款利率")
    loanRateAbove5Year: str | None = Field(default=None, title="5年以上贷款利率")
    mortgateRateBelow5Year: str | None = Field(
        default=None, title="5年以下住房公积金贷款利率")
    mortgateRateAbove5Year: str | None = Field(
        default=None, title="5年以上住房公积金贷款利率")
