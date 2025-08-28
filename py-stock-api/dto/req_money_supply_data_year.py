from pydantic import BaseModel


class ReqMoneySupplyDataYear(BaseModel):
    """
    start_date：开始日期，为空时默认为2015-01-01，包含此日期；
    end_date：结束日期，为空时默认当前日期，包含此日期
    """
    start_date: str
    end_date: str
