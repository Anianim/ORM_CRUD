from flask import jsonify, request
from app.models import Image, ImageStatus
from config import db

# 메인 이미지 조회
def get_main():
    main_image = Image.query.filter_by(type=ImageStatus.main).first()
    if not main_image:
        return jsonify({"message": "메인 이미지를 찾을 수 없습니다."})
    return jsonify({"image": main_image.url})

# 서브 이미지 조회
def get_sub():
    sub_images = Image.query.filter_by(type=ImageStatus.sub).all()
    if not sub_images:
        return jsonify({"message": "서브 이미지를 찾을 수 없습니다."})

    return jsonify({
        "images": [image.url for image in sub_images]
    }), 200

# 이미지 추가
def post_image():
    try:
        data = request.json
        image = Image(
            url=data["url"],
            type=data["type"] 
        )
        db.session.add(image)
        db.session.commit()
        return jsonify({"message": f"이미지 추가 성공"})
    except :
        return jsonify({"message": "이미지 추가 실패"})
