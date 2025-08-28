from pydantic import BaseModel, Field


class ZZ500Stock(BaseModel):
    """
    中证500成分股
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    code_name: str | None = Field(default=None, title="证券名称")
    updateDate: str | None = Field(default=None, title="更新日期")
