from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_Details:Dict[str,str]

    @model_validator(mode='after')

    def validate_emergency_contact(self):
        if self.age>50 and 'emergency' not in self.contact_Details:
            raise ValueError("Patient elder than 50 must have an emergency contact")
        return self


    
def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print("Update")

patient_info={'name':'taha','email':'abc@islamic.com','age':'61',"weight":75.2,"married":True,"allergies":["pollen","Dust"],"contact_Details":{'phone':'234556',"id":"12",'emergency':'2131234'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)
