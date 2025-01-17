from flask import request, jsonify
from app.models import User
from config import db

# 모든 유저 조회 
def get_user():
    users = User.query.all() 
    if users :
        return jsonify([user.to_dict() for user in users])        
    else : 
        return jsonify({"message": "not found user data"})
    
    
# 유저 데이터 저장
def post_user():
    # form 에서 입력된 유저의 데이터를 post 방식으로 전송해주는 API
    user_data = request.json

    # 요청 데이터 검증
    if not user_data:
        return jsonify({"message": "요청 데이터가 없습니다."}), 400

    # 중복 이메일 확인
    existing_user = User.query.filter_by(email=user_data.get("email")).first()
    if existing_user:
        return jsonify({"message": "이미 존재하는 이메일입니다."}), 409

    # 사용자 정보 저장
    try:
        user = User(
            name=user_data.get("name"),
            email=user_data.get("email"),
            age=user_data.get("age"),
            gender=user_data.get("gender"),
        )
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "데이터베이스 오류", "error": str(e)}), 500
