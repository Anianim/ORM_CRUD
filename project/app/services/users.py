from flask import request , jsonify
from app.models import User
from config import db

# 모든 유저 조회 
def get_user():
    users = User.query.all() 
    if users :
        return [user.to_dict() for user in users]        
    else : 
        return {"msg": "not found user data"}
    
    
# 유저 데이터 저장
def post_user():
    user_data = request.json
    user = User
    user.name = user_data["name"]
    user.email = user_data["email"]
    user.age = user_data["age"]
    user.gender = user_data["gender"]
    
    db.session.add(user)
    db.session.commit()
    
    massage = f'{user_data['name']}님 회원가입을 축하합니다.'
    return jsonify({"message": massage})