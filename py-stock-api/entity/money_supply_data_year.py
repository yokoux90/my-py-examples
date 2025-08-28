from pydantic import BaseModel, Field


class MoneySupplyDataYear(BaseModel):
    """
    货币供应量(年底余额)
    """
    statYear: str | None = Field(default=None, title="统计年度")
    m0Year: str | None = Field(default=None, title="年货币供应量M0（亿元）")
    m0YearYOY: str | None = Field(default=None, title="年货币供应量M0（同比）")
    m1Year: str | None = Field(default=None, title="年货币供应量M1（亿元）")
    m1YearYOY: str | None = Field(default=None, title="年货币供应量M1（同比）")
    m2Year: str | None = Field(default=None, title="年货币供应量M2（亿元）")
    m2YearYOY: str | None = Field(default=None, title="年货币供应量M2（同比）")
