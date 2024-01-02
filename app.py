from config import config
from nest.core.app import App

app = App(
    description="PyNest service",
    modules=[]
)


@app.on_event("startup")
def startup():
    config.create_all()
