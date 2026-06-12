from flask import Flask, request, jsonify
from config import Config
from database import db
from models import Users

app = Flask(__name__)

# подключаем конфиг
app.config.from_object(Config)

# подключаем БД
db.init_app(app)

# создаём таблицы
with app.app_context():
    db.create_all()


# ➕ CREATE (добавить пользователя)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    user = Users(
        username=data["username"],
        phone=data["phone"],
        address=data["address"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


# 📋 READ ALL (все пользователи)
@app.route("/users", methods=["GET"])
def get_users():
    users = Users.query.all()
    return jsonify([u.to_dict() for u in users])


# 👤 READ ONE (один пользователь)
@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = Users.query.get_or_404(id)
    return jsonify(user.to_dict())


# ✏️ UPDATE (обновить)
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = Users.query.get_or_404(id)
    data = request.json

    user.username = data["username"]
    user.phone = data["phone"]
    user.address = data["address"]

    db.session.commit()

    return jsonify(user.to_dict())


# ❌ DELETE (удалить)
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = Users.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})


# запуск сервера
if __name__ == "__main__":
    app.run(debug=True)