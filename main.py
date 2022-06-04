from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class alnafi_student_name(BaseModel):
    name : str
    city : Union[str,None] = None
    track : str


@app.post("/get_alnafi_student")
def get_alnafistudent(alnafi_student:alnafi_student_name):
    return alnafi_student

@app.post("/update_alnafi_student")
def get_alnafistudent(alnafi_student:alnafi_student_name):
    alnafi_dic = alnafi_student.dict()
    if alnafi_dic['city'] is None :
        alnafi_dic['city'] = "Dubai"
        return alnafi_dic
    return alnafi_student    

@app.post("/update_alnafi_student_info/{student_id}")
def get_alnafistudent(student_id :int,alnafi_student:alnafi_student_name):
    alnafi_dic = alnafi_student.dict()
    if alnafi_dic['city'] is None :
        alnafi_dic['city'] = "Dubai"
        return {"student_id" : student_id , "student_data" : alnafi_dic}
    return {"student_id" : student_id , "student_data" : alnafi_dic} 