from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class PoiModel(BaseModel):
  id: str
  geom: str
  longitude: float
  latitude: float
  classname: Literal["trash", "crack", "banner", "pothole"] | str
  time: str
  # img_received: bool
  # utm_x: float
  # utm_y: float
  # utm_z: float
  # regionname_1: str
  # regionname_2: str
  # regionname_3: str
  # regionname_4: str | None
  # roadaddr: str
  # roadaddrnum: int
  # isprocessed: bool
  # mb_serial: str
  # mt_serial: str


class GetPoiDataResponseModel(BaseModel):
  rows: list[PoiModel]


class GetPoiDataRequestModel(BaseModel):
  startDate: str
  endDate: str
