from pydantic import BaseModel


class ReqDupontData(BaseModel):
    """
    code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
    year：统计年份，为空时默认当前年；
    quarter：统计季度，可为空，默认当前季度。不为空时只有4个取值：1，2，3，4
    """
    code: str
    year: int
    quarter: int
