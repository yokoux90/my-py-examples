from pydantic import BaseModel


class ReqStockBasic(BaseModel):
    """
    code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
    """
    code: str
