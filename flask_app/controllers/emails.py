from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def get_all_emails(): 
    return render_template('success.html', emails = Email.get_all_emails())


@app.route('/email/add',methods=["POST"])
def add_email():
    if not Email.validate(request.form):
        return redirect('/')
    Email.add_email(request.form)
    session["email"] = request.form["email"]
    return redirect('/success')


@app.route('/delete/<int:id>')
def delete(id):
    Email.delete_email({"id":id})
    return redirect("/success")