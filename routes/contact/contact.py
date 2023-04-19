from typing import Optional
from fastapi import APIRouter, BackgroundTasks, HTTPException

# Library
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException


# Core
from core.config import settings

# Providers
from providers.database import Sesionlocal
from providers.contactSchema import Contact as ContactSchema

# Models
from models.contactModel import Contact
from models.loggerModel import Logger

# Util
from lib.utils import util


api_client = HubSpot(access_token=settings.HUBSPOT_ACCESS_TOKEN)

#object type APIRouter
router_contact = APIRouter(prefix="/contact")

@router_contact.post('/create_contact')
async def create_contact(data: ContactSchema):
    session = Sesionlocal()
    
    # create contact in HubSpot
    try:
        properties = {
            "company": "Orbidi",
            "email": data.email,
            "firstname": data.firstname,
            "lastname": data.lastname,
            "phone": data.phone,
            "website": data.website,
        }
        
        simple_public_object_input = SimplePublicObjectInput(properties=properties)
        api_client.crm.contacts.basic_api.create(simple_public_object_input)
    except ApiException as e:
        session.close()
        return HTTPException(status_code=409, detail=e.reason)
    # save contact in database
    contact = Contact(email= data.email, 
                    firstname = data.firstname,
                    lastname = data.lastname,
                    phone= data.phone,
                    website= data.website)
    session.add(contact)
    session.commit()
    session.refresh(contact)
    session.close()
    return contact


async def sync_contacts():
    session = Sesionlocal()
    contacts = session.query(Contact).filter(Contact.status_clickup == False).all()

    for contact in contacts:
        full_name = f"{contact.firstname} {contact.lastname}"
        email = contact.email
        response = util.createTaskClickUp(email, full_name)
        if response:
            contact.status_clickup = True # type: ignore
            session.add(contact)
            session.commit()
    session.close()

@router_contact.post('/sync_contacts/background')
async def sync_contacts_background(background_tasks: BackgroundTasks, validate_existing: Optional[bool] = False):
    background_tasks.add_task(sync_contacts)
    return {"message": "Sync contacs in the background"}
