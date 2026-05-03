from pydantic import BaseModel, ConfigDict
from typing import Optional, Any
from datetime import datetime

class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
