from . import app
from flask import render_template, request, redirect, url_for, session, flash
import functools

# from werkzeug.security import check_password_hash

slova = ("Super", "Perfekt", "Úža", "Flask")

app.secret_key = (b'\xd6\x1e9U\xadc\xd8\xd8\xeb\xc5\x8a\xf55;+QS\x0b\xa9\xc7\xd9\n>\x13')


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
    if "user" in session:
        return render_template("scitani.html.j2")
    else:
        flash("Na tuto stránku je třeba se přihlásit!", "error")
        return redirect(url_for("login", nextpage=request.full_path))

    a = request.args.get("a")
    b = request.args.get("b")
    try:
        c = int(a) + int(b)
    except (TypeError, ValueError):
        c = ""    
    return render_template("scitani.html.j2", c=c)




@app.route("/odecitani/")
def odecitani():
    if "user" in session:
        return render_template("odecitani.html.j2")
    else:
        flash("Na tuto stránku je třeba se přihlásit!", "error")
        return redirect(url_for("login", nextpage=request.full_path))
    x = request.args.get("x")
    y = request.args.get("y")
    try:
        z = int(x) - int(y)
    except (TypeError, ValueError):
        z = ""    
    return render_template("odecitani.html.j2", z=z)

    


@app.route("/nasobeni/")
def nasobeni():
    if "user" in session:
        return render_template("nasobeni.html.j2")
    else:
        flash("Na tuto stránku je třeba se přihlásit!", "error")
        return redirect(url_for("login", nextpage=request.full_path))

    m = request.args.get("m")
    v = request.args.get("v")
    try:
        e = int(m) * int(v)
    except (TypeError, ValueError):
        e = ""    
    return render_template("nasobeni.html.j2", e=e)




@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html.j2")

    elif request.method == "POST":
        jmeno = request.form.get("jmeno")
        heslo = request.form.get("heslo")
        if jmeno and heslo == "heslo":
            session["user"] = jmeno
            flash("Právě jsi se úspěšně přihlásil!", "uspech")
            nextpage = request.args.get("nextpage")
            if nextpage:
                return redirect(nextpage)
            return redirect(url_for("login"))
        else:
            flash("Nesprávné přihlašovací údaje", "error")
            return redirect(url_for("login"))

@app.route("/logout/")
def logout():
    flash("Byl jsi odhlášen!", "uspech")
    session.pop("user", None)
    return redirect(url_for("login"))
