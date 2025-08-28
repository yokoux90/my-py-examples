from pydantic import BaseModel, Field


class DividendData(BaseModel):
    """
    除权除息信息
    """
    code: str = Field(..., title="证券代码",
                      description="sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳")
    dividPreNoticeDate: str | None = Field(default=None, title="预批露公告日", description="格式: YYYY-MM-DD")
    dividAgmPumDate: str | None = Field(default=None, title="股东大会公告日期", description="格式: YYYY-MM-DD")
    dividPlanAnnounceDate: str | None = Field(default=None, title="预案公告日", description="格式: YYYY-MM-DD")
    dividPlanDate: str | None = Field(default=None, title="分红实施公告日", description="格式: YYYY-MM-DD")
    dividRegistDate: str | None = Field(default=None, title="股权登记告日", description="格式: YYYY-MM-DD")
    dividOperateDate: str | None = Field(default=None, title="除权除息日期", description="格式: YYYY-MM-DD")
    dividPayDate: str | None = Field(default=None, title="派息日", description="格式: YYYY-MM-DD")
    dividStockMarketDate: str | None = Field(default=None, title="红股上市交易日", description="格式: YYYY-MM-DD")
    dividCashPsBeforeTax: str | None = Field(default=None, title="每股股利税前",
                                               description="派息比例分子(税前)/派息比例分母")
    dividCashPsAfterTax: str | None = Field(default=None, title="每股股利税后",
                                            description="派息比例分子(税后)/派息比例分母")
    dividStocksPs: str | None = Field(default=None, title="每股红股")
    dividCashStock: str | None = Field(default=None, title="分红送转",
                                       description="每股派息数(税前)+每股送股数+每股转增股本数")
    dividReserveToStockPs: str | None = Field(default=None, title="每股转增资本")
