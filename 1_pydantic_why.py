# def insert_patient_date(name: str,age: int):
#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError("age cant be negative")
#         else:
#             print(name)
#             print(age)
#             print("Insert into database")
#     else:
#         raise TypeError("Incorrect data type")


# insert_patient_date("taha", 30)


from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Tuple,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of PATIENT",description="Give the name of Patient in less than 50 Char",examples=["Taha","Hanzala"])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int=Field(gt=0,lt=80)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=None,description="Is the Patient is Married or not")]
    allergies:Annotated[Optional[List[str]],Field(max_length=5)]
    contact_Details:Dict[str,str]




def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.email)
    print("Insert into database")

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Insert into database")

patient_info={"name":"Taha",'email':'abc@gmail.com',"linkedin_url":"https://linkedin.com/112233","age":"30","weight":75.2,"married":True,"allergies":["pollen","Dust"],"contact_Details":{'phone':'234556',"ID":"12"}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)
