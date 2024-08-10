import math
from functools import lru_cache

from pathfinding.model import PointModel


def haversine_distance(
  lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
  R = 6371000  # 지구의 반경 (m)

  # 위도와 경도를 라디안으로 변환
  lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

  # Haversine 공식
  dlat = lat2 - lat1
  dlon = lon2 - lon1
  a = (
    math.sin(dlat / 2) ** 2
    + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
  )
  c = 2 * math.asin(math.sqrt(a))

  distance = R * c
  return distance


def calculate_walking_time(source: PointModel, target: PointModel) -> float:
  distance = haversine_distance(
    source.latitude, source.longitude, target.latitude, target.longitude
  )
  average_walking_speed = 1.4 / 3  # m/s (약 5 km/h) 노인이라 절반
  time_seconds = distance / average_walking_speed
  return time_seconds


# @lru_cache(maxsize=None)
def get_walking_time(source: PointModel, target: PointModel) -> float:
  """
  두 PointModel 객체 사이의 도보 이동 시간을 계산합니다.

  :param source: 출발 지점 PointModel
  :param target: 도착 지점 PointModel
  :return: 도보 이동 시간 (초)
  """
  return calculate_walking_time(source, target)
