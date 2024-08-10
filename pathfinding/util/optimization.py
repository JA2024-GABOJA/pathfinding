import heapq
from typing import Callable

from pathfinding.model import PointModel


def get_optimal_path(
  start: PointModel,
  points: list[PointModel],
  limit: float,
  beam_width: int,
  get_distance: Callable[[PointModel, PointModel], float],
) -> list[tuple[float, float]]:
  def get_next_states(
    path: list[PointModel], dist: float, unvisited: set[PointModel]
  ):
    for next_point in unvisited:
      if (
        len(path) > 2
        and path[-1].type == "target"
        and path[-2].type == "target"
        and next_point.type == "target"
      ):
        continue
      new_dist = dist + get_distance(path[-1], next_point)
      if new_dist + get_distance(next_point, start) <= limit:
        new_unvisited = unvisited - {next_point}
        yield (-len(path) - 1, new_dist, path + [next_point], new_unvisited)

  best = [start]
  beam = [(0, 0, [start], set(points))]

  while beam:
    new_beam = []
    for _, dist, path, unvisited in beam:
      new_beam.extend(get_next_states(path, dist, unvisited))
    beam = heapq.nsmallest(beam_width, new_beam)
    if (
      beam and -beam[0][0] > len(best) and beam[0][2][-1].type == "destination"
    ):
      best = beam[0][2]

  return best + [start]
