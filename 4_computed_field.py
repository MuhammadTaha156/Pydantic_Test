from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_Details:Dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi


    
def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print(patient.bmi)
    print("Update")

patient_info={'name':'taha','email':'abc@islamic.com','age':'61',"weight":75.2,'height':1.72,"married":True,"allergies":["pollen","Dust"],"contact_Details":{'phone':'234556',"id":"12",'emergency':'2131234'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)
