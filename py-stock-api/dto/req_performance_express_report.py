from pydantic import BaseModel


class ReqPerformanceExpressReport(BaseModel):
    """
    code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
    start_date：开始日期，为空时默认为2015-01-01，包含此日期；
    end_date：结束日期，为空时默认当前日期，包含此日期
    """
    code: str
    start: str
    end: str
