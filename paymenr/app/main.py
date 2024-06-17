import uvicorn
from fastapi import FastAPI
# from app.config.database import engine
from app.config.database import Base
# from app.auth import authrouter
# from app.users import usersrouter
# from app.review import reviewrouter
# from app.product import productrouter
from app.order.orderrouter import router as orderrouter

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return {"Hello":"hamid"}


app.include_router(authrouter.router, prefix="/api")
app.include_router(usersrouter.router, prefix="/api")
app.include_router(reviewrouter.router, prefix="/api")
app.include_router(productrouter.router, prefix="/api")
app.include_router(orderrouter.router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)