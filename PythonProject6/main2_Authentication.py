from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'Felix Pham'
jwt = JWTManager(app)


# You can protect your web method by requiring a valid JWT token for authentication.
# Use the @jwt_required() decorator to enforce authentication for the specific route.
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access to this endpoint is protected, and the user must have a valid JWT token
    return jsonify(logged_in_as='current_user'), 200


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Validate user credentials (example: check against a database)
    if username == 'user' and password == 'password':
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401
if __name__ == '__main__':
    app.run(debug=True)