from typing import Literal

from pydantic import BaseModel, Field


class ReqDividendData(BaseModel):
    """
    code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
    year：年份，如：2017。此参数不可为空；
    yearType：年份类别，默认为"report":预案公告年份，可选项"operate":除权除息年份。此参数不可为空
    """
    code: str
    year: str
    yearType: Literal["report", "operate"] = Field(default="report", title="年份类别", description="默认为report: 预案公告年份，可选项operate: 除权除息年份")