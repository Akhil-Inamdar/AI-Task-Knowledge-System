# from fastapi import FastAPI

# app = FastAPI(title="AI Task Management System")

# @app.get("/")
# def home():
#     return {"message": "Backend is running successfully!"}

# from fastapi import FastAPI
# from app.routers import document

# app = FastAPI(title="AI Task Management System")

# app.include_router(document.router)

# @app.get("/")
# def home():
#     return {"message": "Backend is running successfully!"}

# from fastapi import FastAPI
# from app.routers import document
# # from app.routers import search

# app = FastAPI(title="AI Task Management System")

# app.include_router(document.router)
# # app.include_router(search.router)


# @app.get("/")
# def home():
#     return {
#         "message": "Backend is running successfully!"
#     }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import task
from app.routers import auth
from app.routers import document
from app.routers import search
from app.routers import dashboard

app = FastAPI(
    title="AI Task Management System"
)

# ----------------------------
# CORS Configuration
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Routers
# ----------------------------
app.include_router(auth.router)
app.include_router(document.router)
app.include_router(search.router)
app.include_router(task.router)
app.include_router(dashboard.router)

# ----------------------------
# Home Route
# ----------------------------
@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }