from datetime import datetime, timedelta

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathfinding.model import PointModel
from pathfinding.service import get_destinations, get_trashes
from pathfinding.util import get_optimal_path, get_walking_time

app = FastAPI()

origins = [
  "*",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

destination_points = get_destinations()
N_BEAM = 1000


@app.get("/findpath")
async def find_path(
  current_longitude: float = 129.349714,
  current_latitude: float = 36.013493,
  walking_duration_sec: int = 60 * 60 * 2,  # seconds
  start_date: str = (datetime.now() - timedelta(days=2)).strftime("%y%m%d"),
  end_date: str = datetime.now().strftime("%y%m%d"),
):
  trashes = get_trashes(start_date, end_date)
  current = PointModel(
    latitude=current_latitude,
    longitude=current_longitude,
    type="current",
  )
  path = get_optimal_path(
    current,
    trashes + destination_points,
    walking_duration_sec,
    N_BEAM,
    get_walking_time,
  )
  print(path)

  return path
