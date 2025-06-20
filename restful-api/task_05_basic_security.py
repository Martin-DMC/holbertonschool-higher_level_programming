"""
in this module i define a api what in charge of all security of the this
raoutes, with libraries like httpauth, security of werkzeug and
jwt extend of flask.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
                "username": "user1",
                "password": generate_password_hash("password"),
                "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}
###########################
"""
in this section i set up the response of all errors will it happened.
"""


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

######################################################


"""
in this section. i set up these function that helps me
to verify if the access token is ok and also to verify the password hash
"""


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user['username']


@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {'role': user['role']}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        user = users.get(username)
        pswd = user['password']
        if check_password_hash(pswd, password):
            return user
        return None
    return None

################################################


"""
in this section. i define the routes with some
decoration for associate to the correct functions
"""


@app.route("/login", methods=["POST"])
@auth.login_required
def login():
    user = auth.current_user()


    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    # Access the identity of the current user with get_jwt_identity
    claims = get_jwt()
    return {'message': "JWT Auth: Access Granted"}, 200


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return {'message': "Basic Auth: Access Granted"}, 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    user = get_jwt()
    if user and user.get('role') == 'admin':
        return {'message': 'Admin Access: Granted'}, 200
    return {'error': 'Admin access required'}, 403


if __name__ == '__main__':
    app.run(debug=True)
