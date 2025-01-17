from flask import  request ,jsonify , Blueprint
from flask.views import MethodView
from app.services import questions, images, users , choices , answers



# 블루프린터 객체 생성 
image_blp = Blueprint('images' , __name__, url_prefix='/image')
user_blp = Blueprint('signup', __name__, url_prefix='/signup')
question_blp = Blueprint('question', __name__, url_prefix='/question')
questions_blp = Blueprint('questions', __name__, url_prefix='/questions')
choice_blp = Blueprint('choice', __name__, url_prefix='/choice')
submit_blp = Blueprint('submit', __name__, url_prefix='/submit')


# 메인 이미지 가져오는 API
@image_blp.route('/main', methods=["GET"])
def get_main_image():        
    return images.get_main()

# 서브 이미지 가져오는 API
@image_blp.route('/sub', methods=["GET"])
def get_sub_image():        
    images.get_main()
    return images.get_sub()

# 이미지 등록 API
@image_blp.route('/', methods=["POST"])
def create_image():
    return images.post_image()

# 회원가입 API 
@user_blp.route('/', methods=["POST"])
def signup_user():
    users.post_user()
    message = f"{request.json.get('name')}' 님 회원가입 축하드립니다.'"
    return jsonify({"message": message}), 200

# 질문 조회 API
@question_blp.route('/<int:question_id>', methods=["GET"])
def get_question(question_id):
    print(question_id)
    return questions.get_question(question_id)

# 질문 생성 API
@question_blp.route('/', methods=["POST"])
def CreateQuestionAPI():   
    return questions.post_question()

# 질문 총개수를 구하는 API
@questions_blp.route('/count', methods=["GET"])
def count_question():
    return questions.count()

# 초이스를 가져오는 API 
@choice_blp.route('/<int:question_id>', methods=["GET"])
def get_choice(question_id):
    print(question_id)
    return choices.get_choices(question_id)

# 초이스 등록하는 API
@choice_blp.route('/', methods=["POST"])
def post_choice():
    return choices.post_choice()      

# 제출 하는 API
@submit_blp.route( '/' , methods=["POST"])
def post_submit():
    return answers.submit()

