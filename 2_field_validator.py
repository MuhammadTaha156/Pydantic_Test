from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_Details:Dict[str,str]

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domians=['mzn.com','islamic.com']
        # abc@gmail.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domians:
            raise ValueError("Not valid domain")
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.capitalize()
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_Age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in b/w 0 and 100 ")


def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print("Update")

patient_info={'name':'taha','email':'abc@islamic.com','age':'30',"weight":75.2,"married":True,"allergies":["pollen","Dust"],"contact_Details":{'phone':'234556',"id":"12"}}

patient1=Patient(**patient_info)

update_patient_data(patient1)

