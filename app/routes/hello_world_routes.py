from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__, url_prefix="/hello/")

@hello_world_bp.get("/hi")
def say_hello():
    return "<h1>Hello World!</h1><p>This one is made with \"get\"</p>"

@hello_world_bp.route("/", methods=['GET'])
def say_hello_again():
    return "<h1>Hello World!</h1><p>This one is made with \"route\"</p>"

hello_world_bp.add_url_rule("/hey", view_func=say_hello)

@hello_world_bp.get("JSON/")
def some_json():
    return {
        "name": "Tatiana",
        "academy": "Ada Developers Academy",
        "class": "Sphinx",
    }
