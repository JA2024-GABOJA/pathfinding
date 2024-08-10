from typing import Generic, Type, TypeVar

import requests
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class Request(Generic[T]):
  def __init__(self, ResponseModel: Type[T]) -> None:
    self.ResponseModel = ResponseModel

  def get(self, endpoint: str) -> T:
    try:
      response = requests.get(endpoint)
      response.raise_for_status()
      return self.ResponseModel.model_validate(response.json())

    except requests.exceptions.HTTPError as e:
      raise Exception(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError as e:
      raise Exception(f"Connection error: {e}")
    except requests.exceptions.Timeout as e:
      raise Exception(f"Timeout error: {e}")
    except requests.exceptions.RequestException as e:
      raise Exception(f"Request error: {e}")

  def post(self, endpoint: str, body: BaseModel) -> T:
    try:
      response = requests.post(endpoint, json=body.model_dump())
      response.raise_for_status()
      return self.ResponseModel.model_validate(response.json())

    except requests.exceptions.HTTPError as e:
      raise Exception(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError as e:
      raise Exception(f"Connection error: {e}")
    except requests.exceptions.Timeout as e:
      raise Exception(f"Timeout error: {e}")
    except requests.exceptions.RequestException as e:
      raise Exception(f"Request error: {e}")
