from datetime import datetime
import time
from typing import Optional
import uuid
from celery import Celery
from sqlmodel import Session, select
from db import engine
from model import Event, EventStatus, Job

# Celery Pool类型：
#    1. prefork: (Default) (Linux/Unix)每个子进程处理一个任务
#    2. eventlet: (Linux/Unix)使用事件驱动的方式进行并发处理，适合I/O密集型
#    3. gevent：(Linux/Unix)与eventlet类似，但使用gevent来实现协程
#    4. solo： 单线程池，适合调试和开发阶段
#    5. threads：多线程池
#
# Windows系统下必须指定-P threads / -P solo
# celery -A tasks worker -P solo --loglevel=INFO

app = Celery(
    "tasks",
    broker="redis://:example@localhost:6379/0",
    backend="redis://:example@localhost:6379/0",
)


@app.task(trail=True)
def add(x: int, y: int):
    time.sleep(1)
    return x + y


@app.task(trail=True)
def create_job(job_name: str) -> str:
    with Session(engine) as session:
        job_id = uuid.uuid4()
        new_job = Job(
            job_id=job_id,
            job_name=job_name,
            events=[
                Event(
                    job_id=job_id,
                    status=EventStatus.Pending,
                )
            ],
        )
        session.add(new_job)
        session.commit()
        session.refresh(new_job)

        return new_job.model_dump_json()


@app.task(trail=True)
def update_job(job_id: str) -> Optional[str]:
    with Session(engine) as session:
        event = session.exec(select(Event).where(Event.job_id == job_id)).first()
        if event is None:
            return None
        match event.status:
            case EventStatus.Pending:
                event.status = EventStatus.Done
            case _:
                event.status = EventStatus.Failed

        session.add(event)
        session.commit()

        job = session.get(Job, job_id)
        if job is None:
            return None
        job.completed_at = datetime.now()
        session.add(job)
        session.commit()
        session.refresh(job)

        return job.model_dump_json()


@app.task(trail=True)
def delete_job(job_id: str) -> Optional[str]:
    with Session(engine) as session:
        job = session.get(Job, job_id)
        if job is None:
            return None

        session.delete(job)
        session.commit()

        return job.model_dump_json()
