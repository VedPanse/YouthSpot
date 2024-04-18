from flask import Flask, render_template, request, redirect
import os
import time
import stat

app = Flask(__name__)

def return_error():
    return render_template("ErrorTemplates/NotFound.html")


@app.route("/")
@app.route("/index.html")
def start_session():
    return render_template("index.html")

@app.route("/log-in.html")
def load_log_in():
    return render_template("log-in.html")


@app.route("/log-in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        username: str = request.form.get("username")
        password: str = request.form.get("password")
        return f"Username: {username}, Password: {password}"
    return return_error()

@app.route("/sign-up.html")
def load_sign_up(msg=''):
    return render_template("sign-up.html", msg=msg)

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            # Passwords don't match, reload sign-up page with error message
            return load_sign_up(msg="Password mismatched")
        else:
            # Passwords match, redirect to events page
            return redirect("/events.html")  # Use redirect to navigate to events page
    
    # GET request or no error message specified, return error page
    return return_error()



@app.route("/events.html")
def load_events():
    return render_template("events.html")


if __name__ == "__main__":
    app.run(debug=True)