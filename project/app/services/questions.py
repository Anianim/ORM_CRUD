from flask import jsonify, request
from app.models import Question, Choices, Image
from config import db

#특정 질문 조회
def get_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        return jsonify({"message": "질문을 찾을 수 없습니다."})
    image = Image.query.get(question.image_id)

    return jsonify({
            "question": {
                "id": question.id,
                "title": question.title,
                "image": {"url": image.url if image else None},
                "choices": [
            {
                "id": choice.id,
                "text": choice.text,
                "is_active": choice.is_active,
                "sqe": choice.sqe
            }
            for choice in Choices.query.filter_by(question_id=question.id).all()
        ]}})

#질문 개수 확인
def count():
    total = Question.query.count()
    return jsonify({"total": total}), 200

#질문 추가
def post_question():
    data = request.json
    if data :
        question = Question(
            title=data.get("title"),
            sqe=data.get("sqe"),
            image_id=data.get("image_id")
        )
        db.session.add(question)
        db.session.commit()
    else : 
        return jsonify({"message": "데이터가 없습니다."})
    return jsonify({"message": "질문이 성공적으로 추가되었습니다.", "question_id": question.id})