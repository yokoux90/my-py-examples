from typing import Annotated, List
from celery.result import AsyncResult
from fastapi import Body, HTTPException
from fastapi.routing import APIRouter
from loguru import logger
from sqlmodel import select
from db import SessionDep
from model import Event, Job
import tasks
from dto import JobRequest, JobResponse, JobUpdate


router = APIRouter(prefix="/api", tags=["Celery"])


@router.get(
    "/jobs",
    response_model=List[JobResponse],
    description="Fetch from database directly",
)
def get_jobs(session: SessionDep):
    jobs = session.exec(select(Job)).all()
    return jobs


@router.post(
    "/jobs",
    response_model=JobResponse,
    description="Send data to celery pool, and wait result",
)
def create_job(
    job: Annotated[JobRequest, Body(example={"job_name": "Mock Task"})],
):
    task: AsyncResult = tasks.create_job.delay(job.job_name)

    if task.ready():
        return task.result

    result = task.get(timeout=30)
    if result is None:
        return HTTPException(status_code=500, detail="Celery task timeout.")
    logger.info(f"Task result: {result}")
    return Job.model_validate_json(result)


@router.put(
    "/jobs",
    response_model=JobResponse,
    description="Send data to celery pool, and wait result",
)
def update_job(job: Annotated[JobUpdate, Body()]):
    task: AsyncResult = tasks.update_job.delay(job.job_id)

    if task.ready():
        return task.result

    result = task.get(timeout=30)
    if result is None:
        return HTTPException(status_code=500, detail="Celery task timeout.")
    logger.info(f"Task result: {result}")
    return Job.model_validate_json(result)


@router.delete(
    "/jobs",
    response_model=JobResponse,
    description="Send data to celery pool, and wait result",
)
def delete_job(job: Annotated[JobUpdate, Body()]):
    task: AsyncResult = tasks.delete_job.delay(job.job_id)

    if task.ready():
        return task.result

    result = task.get(timeout=30)
    if result is None:
        return HTTPException(status_code=500, detail="Celery task timeout.")
    logger.info(f"Task result: {result}")
    return Job.model_validate_json(result)
