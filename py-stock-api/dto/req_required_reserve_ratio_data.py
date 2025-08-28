from pydantic import BaseModel, Field


class ReqRequiredReserveRatioData(BaseModel):
    """
    start_date：开始日期，为空时默认为2015-01-01，包含此日期；
    end_date：结束日期，为空时默认当前日期，包含此日期
    yearType:年份类别，默认为0，查询公告日期；1查询生效日期
    """
    start_date: str | None = None
    end_date: str | None = None
    year_type: str = Field(default="0")
