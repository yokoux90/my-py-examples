from pydantic import BaseModel, Field


class StockIndustry(BaseModel):
    """
    行业分类
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    code_name: str | None = Field(default=None, title="证券名称")
    updateDate: str | None = Field(default=None, title="更新日期")
    industry: str | None = Field(default=None, title="所属行业")
    industryClassification: str | None = Field(default=None, title="所属行业类别")
