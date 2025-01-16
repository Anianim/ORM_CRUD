from flask import jsonify, request
from app.models import Answer, User, Choices
from config import db

# 답변 저장
def submit():
    try:
        answers_data = request.json  
        for answer_data in answers_data:
            user_id = answer_data["userId"]
            choice_id = answer_data["choiceId"]

            user = User.query.get(user_id)
            choice = Choices.query.get(choice_id)
            if not user:
                return jsonify({"message": f"{user_id}를 찾을 수 없습니다."})
            if not choice:
                return jsonify({"message": f"{choice_id}를 찾을 수 없습니다."})

            # 답변 저장
            answer = Answer(user_id=user_id, choice_id=choice_id)
            db.session.add(answer)

        db.session.commit()
        return jsonify({"message": f"Success Submit"})
    except :
        return jsonify({"message": "Fail Submit"})
