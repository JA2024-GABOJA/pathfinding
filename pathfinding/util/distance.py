from numpy import ndarray

from pathfinding.model import PointModel

from .walking import get_walking_time


def get_distance_matrix(points: list[PointModel]) -> ndarray:
  """
  주어진 PointModel 객체들 사이의 거리 행렬을 계산합니다.

  :param points: PointModel 객체 리스트
  :return: 거리 행렬
  """
  n = len(points)
  distance_matrix = ndarray((n, n))
  for source, source_index in points:
    for target, target_index in points:
      distance = 0
      if source_index != target_index:
        distance = get_walking_time(source, target)
      distance_matrix[source_index, target_index] = distance
  return distance_matrix
