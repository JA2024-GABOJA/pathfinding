from __future__ import annotations

from typing import Literal, Optional

from pydantic import (
  BaseModel,
  Field,
  model_validator,
)


class PointModel(BaseModel):
  latitude: float
  longitude: float
  type: Literal["current", "target", "destination"]
  id: int | None = None
  name: Optional[str] = None
  address: Optional[str] = None

  @model_validator(mode="before")
  def check_name_and_address(cls, values):
    type_ = values.get("type")
    name = values.get("name")
    address = values.get("address")
    id = values.get("id")

    if type_ == "destination":
      if not name or not address:
        raise ValueError(
          "name and address must be provided when type is 'destination'"
        )
    elif type_ == "target":
      if not id:
        raise ValueError("id must be provided when type is 'target'")
    else:
      if name is not None or address is not None:
        raise ValueError(
          "name and address should only be provided when type is 'destination'"
        )

    return values

  def __hash__(self) -> int:
    return hash((self.latitude, self.longitude, self.type))
