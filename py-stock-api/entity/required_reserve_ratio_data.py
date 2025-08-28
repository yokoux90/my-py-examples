from pydantic import BaseModel, Field


class RequiredReserveRatioData(BaseModel):
    """
    存款准备金率
    """
    pubDate: str | None = Field(default=None, title="公告日期")
    effectiveDate: str | None = Field(
        default=None, title="生效日期")
    bigInstitutionsRatioPre: str | None = Field(
        default=None, title="人民币存款准备金率：大型存款类金融机构 调整前")
    bigInstitutionsRatioAfter: str | None = Field(
        default=None, title="人民币存款准备金率：大型存款类金融机构 调整后")
    mediumInstitutionsRatioPre: str | None = Field(
        default=None, title="人民币存款准备金率：中小型存款类金融机构 调整前")
    mediumInstitutionsRatioAfter: str | None = Field(
        default=None, title="人民币存款准备金率：中小型存款类金融机构 调整后")
