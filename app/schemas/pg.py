from pydantic import BaseModel, ConfigDict


class PGCreate(BaseModel):
    name: str
    address: str


class PGResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    address: str
    owner_id: int