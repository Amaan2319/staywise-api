from pydantic import BaseModel, ConfigDict


class RoomCreate(BaseModel):
    room_number: str
    capacity: int


class RoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    room_number: str
    capacity: int
    occupied_beds: int
    pg_id: int