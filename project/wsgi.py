from app import create_app
from flask import jsonify

app = create_app()

@app.route('/', methods=['GET'])
def check_connection():
    return jsonify({"message": "Success Connect"}) 


if __name__ == "__main__":
    app.run(debug=True)