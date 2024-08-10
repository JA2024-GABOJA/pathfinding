from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/findpath")
async def find_path(
  current_longitude: float, current_latitude: float, walking_duration: int
):
  return {
    "path": [
      {"longitude": 0.0, "latitude": 0.0},
      {"longitude": 1.0, "latitude": 1.0},
    ]
  }
