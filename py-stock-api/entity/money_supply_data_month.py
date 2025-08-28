from pydantic import BaseModel, Field


class MoneySupplyDataMonth(BaseModel):
    """
    货币供应量
    """
    statYear: str | None = Field(default=None, title="统计年度")
    statMonth: str | None = Field(default=None, title="统计月份")
    m0Month: str | None = Field(default=None, title="货币供应量M0（月）")
    m0YOY: str | None = Field(default=None, title="货币供应量M0（同比）")
    m0ChainRelative: str | None = Field(default=None, title="货币供应量M0（环比）")
    m1Month: str | None = Field(default=None, title="货币供应量M1（月）")
    m1YOY: str | None = Field(default=None, title="货币供应量M1（同比）")
    m1ChainRelative: str | None = Field(default=None, title="货币供应量M1（环比）")
    m2Month: str | None = Field(default=None, title="货币供应量M2（月）")
    m2YOY: str | None = Field(default=None, title="货币供应量M2（同比）")
    m2ChainRelative: str | None = Field(default=None, title="货币供应量M2（环比）")
