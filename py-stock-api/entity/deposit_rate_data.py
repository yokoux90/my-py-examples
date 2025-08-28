from pydantic import BaseModel, Field


class DepositRateData(BaseModel):
    """
    存款利率
    """
    pubDate: str | None = Field(default=None, title="发布日期")
    demandDepositRate: str | None = Field(default=None, title="活期存款(不定期)")
    fixedDepositRate3Month: str | None = Field(default=None, title="定期存款(三个月)")
    fixedDepositRate6Month: str | None = Field(default=None, title="定期存款(半年)")
    fixedDepositRate1Year: str | None = Field(
        default=None, title="定期存款整存整取(一年)")
    fixedDepositRate2Year: str | None = Field(
        default=None, title="定期存款整存整取(二年)")
    fixedDepositRate3Year: str | None = Field(
        default=None, title="定期存款整存整取(三年)")
    fixedDepositRate5Year: str | None = Field(
        default=None, title="定期存款整存整取(五年)")
    installmentFixedDepositRate1Year: str | None = Field(
        default=None, title="零存整取、整存零取、存本取息定期存款(一年)")
    installmentFixedDepositRate3Year: str | None = Field(
        default=None, title="零存整取、整存零取、存本取息定期存款(三年)")
    installmentFixedDepositRate5Year: str | None = Field(
        default=None, title="零存整取、整存零取、存本取息定期存款(五年)")
