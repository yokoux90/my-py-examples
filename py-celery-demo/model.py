from datetime import datetime
from enum import Enum
from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field


class EventStatus(Enum):
    Pending = "Pending"
    Suspend = "Suspend"
    Failed = "Failed"
    Done = "Done"


# Many-To-Many Example

# class JobEventLink(SQLModel, table=True):
#     job_id: Optional[str] = Field(default=None, foreign_key="job.job_id", primary_key=True)
#     event_id: Optional[int] = Field(default=None, foreign_key="event.id", primary_key=True)

# class Job(SQLModel, table=True):
#     job_id: str = Field(..., primary_key=True)
#     job_name: str = Field(...)
#     started_at: datetime = Field(default=datetime.now())
#     completed_at: Optional[datetime] = Field(default=None)

#     events: List["Event"] = Relationship(back_populates="jobs", link_model=JobEventLink)

# class Event(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     job_id: str = Field(..., foreign_key="job.job_id")
#     status: EventStatus = Field(default=EventStatus.Pending)
#     description: Optional[str] = Field(default=None)

#     jobs: List[Job] = Relationship(back_populates="events", link_model=JobEventLink)


# One-To-Many Example
class Job(SQLModel, table=True):
    """
    One Job <- Multiple Events
    """

    job_id: str = Field(..., primary_key=True)
    job_name: str = Field(...)
    started_at: datetime = Field(default=datetime.now())
    completed_at: Optional[datetime] = Field(default=None)

    events: List["Event"] = Relationship(back_populates="job", cascade_delete=True)


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: str = Field(..., foreign_key="job.job_id")
    status: EventStatus = Field(default=EventStatus.Pending)
    description: Optional[str] = Field(default=None)

    job: Optional[Job] = Relationship(back_populates="events")
