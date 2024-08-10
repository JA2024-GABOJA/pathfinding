from typing import Literal

from pydantic import BaseModel


class PointModel(BaseModel):
  latitude: float
  longitude: float
  type: Literal["current", "target", "destination"]
