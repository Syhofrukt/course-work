from pydantic import BaseModel


class GetPeriodData(BaseModel):
    bank: str
    date_from: str
    date_to: str
    currency: str


class GetData(BaseModel):
    bank: str
