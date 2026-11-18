from fastapi import FastAPI, HTTPException
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import Employee, Student, Course, Teacher

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/students/{id}")
async def read_students(id: int):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(Student, id)
        if emp is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return {"message": emp}


@app.post("/students")
async def create_student(student : Student):
    with Session(engine) as session:
        session.add(student)
        session.commit()
        session.refresh(student)

        return {"message": 'created'}

@app.get("/courses/{id}")
async def read_courses(id: int):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(Course, id)
        if emp is None:
            raise HTTPException(status_code=404, detail="Course not found")
        return {"message": emp}


@app.post("/courses")
async def create_course(course: Course):
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
        return {"message": 'created'}

@app.get("/teachers/{id}")
async def read_teachers(id: int):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(Teacher, id)
        if emp is None:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return {"message": emp}

@app.post("/teachers")
async def create_teacher(teacher: Teacher):
    with Session(engine) as session:
        session.add(teacher)
        session.commit()
        session.refresh(teacher)
        return {"message": 'created'}
