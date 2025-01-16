from app import create_app
from flask import jsonify

application = create_app()

@application.route('/', methods=['GET'])
def check_connection():
    return jsonify({"message": "Success Connect"}) 


if __name__ == "__main__":
    application.run(debug=True)