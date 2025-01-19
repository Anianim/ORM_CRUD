from flask import request, jsonify
from app.models import Choices
from config import db

# 질문의 choice 조회 
def get_choices(question_id):
    # 데이터베이스에서 선택지 가져오기
    choices = Choices.query.filter_by(question_id=question_id).all()

    if choices:
        # 선택지가 존재하는 경우
        return jsonify({
            "choices": [
                {
                    "id": choice.id,
                    "text": choice.text,  
                    "is_active": choice.is_active,
                    "sqe": choice.sqe
                }
                for choice in choices
            ]
        }), 200
    else:
        # 선택지가 없는 경우
        return jsonify({"message": "질문에 등록된 초이스가 없습니다."}), 404


def post_choice():
    data = request.json
    
    if data :
        choice = Choices(
            text = data.get("text"),
            sqe = data.get("sqe"),
            question_id = data.get("question_id")
        )
        db.session.add(choice)
        db.session.commit()
    else : 
        return jsonify({"message": "데이터가 없습니다."})
    
    return jsonify({"message": "선택지가 성공적으로 추가되었습니다."}), 200

