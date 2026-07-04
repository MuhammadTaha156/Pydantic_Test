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


from pydantic import BaseModel
from typing import List,Dict,Tuple

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_Details:Dict[str,str]




def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Insert into database")

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Insert into database")

patient_info={"name":"Taha","age":"30","weight":"75.2","married":True,"allergies":["pollen","Dust"],"contact_Details":{'email':'abc@gmail.com','phone':'234556',"ID":"12"}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
