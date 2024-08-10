from functools import lru_cache

from pathfinding.model import (
  GetPoiDataRequestModel,
  GetPoiDataResponseModel,
  PointModel,
)
from pathfinding.util.requests import Request


@lru_cache(maxsize=None)
def get_trash_points(startDate: str, endDate: str) -> list[PointModel]:
  response = Request(GetPoiDataResponseModel).post(
    "http://webviewer.mobiltech.io:18084/poviewer/GetPoiData",
    GetPoiDataRequestModel(startDate=startDate, endDate=endDate),
  )
  return [
    PointModel(latitude=r.latitude, longitude=r.longitude, type="target")
    for r in response.rows
    if r.classname == "trash"
  ]
