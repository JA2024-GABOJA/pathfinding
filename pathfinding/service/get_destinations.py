import pandas as pd

from pathfinding.model import PointModel

df_police = pd.read_csv("pathfinding/assets/police.csv")


def get_destinations():
  return (
    [
      # 경찰서
      PointModel(
        latitude=row["latitude"],
        longitude=row["longitude"],
        type="destination",
        name=f"{row["관서명"]} {row["구분"]}",
        address=row["주소"],
      )
      for _, row in df_police.iterrows()
    ]
    + [
      # 주민센터
    ]
  )
