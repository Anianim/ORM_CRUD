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

# 메인 이미지 추가
def post_image():
    try:
        data = request.json

        # Enum 변환
        image_type = ImageStatus[data.get("type")] if data.get("type") else None

        # 이미지 객체 생성
        image = Image(
            url=data.get("url"),
            type=image_type
        )

        # 데이터베이스에 추가
        db.session.add(image)
        db.session.commit()

        # 성공적인 응답 반환
        return jsonify({
            "message": f"{image.id}번째 {image.type.value} 이미지 추가 완료",
        }), 201

    except KeyError as e:
        # Enum 변환 실패 시 KeyError 발생
        return jsonify({"message": f"유효하지 않은 이미지 유형: {e}"}), 400

    except Exception as e:
        # 기타 예외 처리
        db.session.rollback()
        return jsonify({"message": "이미지 추가 실패", "error": str(e)}), 500
    
def post_sub_image():
    try:
        data = request.json

        # Enum 변환
        image_type = ImageStatus[data.get("type")] if data.get("type") else None

        # 이미지 객체 생성
        image = Image(
            url=data.get("url"),
            type=image_type ,
            sqe=data.get("sqe")
        )

        # 데이터베이스에 추가
        db.session.add(image)
        db.session.commit()

        # 성공적인 응답 반환
        return jsonify({
            "message": f"{image.id}번째 {image.type.value} 이미지 추가 완료",
        }), 201

    except KeyError as e:
        # Enum 변환 실패 시 KeyError 발생
        return jsonify({"message": f"유효하지 않은 이미지 유형: {e}"}), 400

    except Exception as e:
        # 기타 예외 처리
        db.session.rollback()
        return jsonify({"message": "이미지 추가 실패", "error": str(e)}), 500