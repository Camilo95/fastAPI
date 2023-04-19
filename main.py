#Imports
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from models import contactModel, loggerModel 
from providers.database import engine_local, engine_remote

#Object api routes
# from routes.contact import contact as main_contact
from routes.contact import contact as main_contact

#Create tables 
contactModel.Base.metadata.create_all(bind=engine_local)
loggerModel.Base.metadata.create_all(bind=engine_remote)

#Object fast API
app = FastAPI(title="FastAPI",
             description="api for tecnical test using like libraries: postgresSQL, Click Up, and HubSpot",
             version="1.0")

#Include the object on APIROUTER
app.include_router(main_contact.router_contact) 
# app.include_router(mainproduct.routerproduct)


#this route redirect to documentation
@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")