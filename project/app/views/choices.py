from flask import request
from app.models import Choices
from config import db

# 질문의 choice 조회 
def get_choices(question_id):
    choices = Choices.query.filter_by(question_id = question_id).all() 
    if choices :
        return [choice.to_dict() for choice in choices]        
    else : 
        return {"msg": "Not found choices data "}
    
# 관리자 기능 
#def push_choices():
