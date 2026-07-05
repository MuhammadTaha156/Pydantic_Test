from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated


class Address(BaseModel):
    city:str
    state:str
    pin:str


class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
    
address_dict={'city':'Wah cantt','state':'punjab','pin':'314742'}

address1=Address(**address_dict)

patient_info={'name':'taha','gender':'male','age':'61','address':address1}

def update_patient_data(patient:Patient):

    print(patient.name)

    print(patient.age)
    print(patient.address)
    print(patient.address.pin)

    print("Update")


patient1=Patient(**patient_info)

update_patient_data(patient1)