from flask import  request ,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from app.views import questions, images, users , choices , answers



# 블루프린터 
image_blp = Blueprint('images' , __name__, url_prefix='/image')
user_blp = Blueprint('users', __name__, url_prefix='/signup')
question_blp = Blueprint('question', __name__, url_prefix='/question')
questions_blp = Blueprint('questions', __name__, url_prefix='/questions')
choice_blp = Blueprint('choice', __name__, url_prefix='/choice')
submit_blp = Blueprint('submit', __name__, url_prefix='/submit')



@image_blp.route('/<string:main>')
class ImageAPI(MethodView):
    def get(self, main):        
        if main == 'main':
            return images.get_main()
        else:
            return images.get_sub()

@image_blp.route('/')
class CreateImageAPI(MethodView):
    def post(self):
        images.post_image()


@user_blp.route('/')
class UsersAPI(MethodView):
    def post(self):
        user_data = request.json
        try:
            users.post_user(user_data)
        except:
            return jsonify({"message": "유저 입력에 실패했습니다."})


@question_blp.route('/<int:question_id>')
class QuestionsAPI(MethodView):
    def get(self, question_id):
        questions.get_question(question_id)


@question_blp.route('/')
class CreateQuestionAPI(MethodView):   
    def post(self):
        try:
            question = questions.post_question()
            return {"message": "Question added successfully!"}
        except:
            return {"error": "질문 등록실패"}


@questions_blp.route('/count')
class CountAPI(MethodView):
    def get(self):
        questions.count()


@choice_blp.route('/<int:question_id>')
class ChoiceAPI(MethodView):
    def get(self, question_id=None):
        choice = choices.get_choices(question_id)


@choice_blp.route('/')
class CreateChoiceAPI(MethodView):   
    def post(self):
        try:
            question_title = request.json.get('title')
            image_id = request.json.get('image_id')
            sqe = request.json.get('sqe')
            questions.post_question(question_title, image_id, sqe)
            return {"message": "Question added successfully!"}, 200
        except:
            return {"error": "보기 등록실패"}, 500


@submit_blp.route('/')
class SubmitAPI(MethodView):
    def post(self):
        answers.submit()

# Url_rule 과 Blueprint 연결
# question_blp.add_url_rule('/<int:question_id>', view_func = QuestionsAPI.as_view('questions_api'))
# question_blp.add_url_rule('/count', view_func = CountAPI.as_view('questions_count_api'))
# question_blp.add_url_rule('/', view_func = CreateQuestionAPI.as_view('make_question_api'))
# user_blp.add_url_rule('/', view_func = UsersAPI.as_view('users_api'))
# choice_blp.add_url_rule('/<int:question_id>', view_func = ChoiceAPI.as_view('choice_api'))
# choice_blp.add_url_rule('/', view_func = CreateChoiceAPI.as_view('make_choice_api'))
# image_blp.add_url_rule('/<string:main>', view_func=ImageAPI.as_view('image_api'))
# submit_blp.add_url_rule('/', view_func = UsersAPI.as_view('answer_api'))
