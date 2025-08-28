from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from model import Event


class JobRequest(BaseModel):
    job_name: str


class JobUpdate(BaseModel):
    job_id: str


class JobResponse(BaseModel):
    job_id: str
    job_name: str
    started_at: datetime
    completed_at: Optional[datetime] = None

    events: List["Event"] = []
