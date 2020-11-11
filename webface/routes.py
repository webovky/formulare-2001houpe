from . import app
from flask import render_template, request, redirect, url_for, session
import functools

# from werkzeug.security import check_password_hash

slova = ("Super", "Perfekt", "Úža", "Flask")


def prihlasit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for("login", url=request.path))

    return wrapper


@app.route("/", methods=["GET"])
def scitani():
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        c = int(a) + int(b)
    except (TypeError, ValueError):
        c = ""    
    return render_template("scitani.html.j2", c=c)




@app.route("/odecitani/")
def odecitani():
    x = request.args.get("x")
    y = request.args.get("y")
    try:
        z = int(x) - int(y)
    except (TypeError, ValueError):
        z = ""    
    return render_template("odecitani.html.j2", z=z)
    


@app.route("/nasobeni/")
def nasobeni():
    m = request.args.get("m")
    v = request.args.get("v")
    try:
        e = int(m) * int(v)
    except (TypeError, ValueError):
        e = ""    
    return render_template("nasobeni.html.j2", e=e)



