from flask import Flask,request, render_template, url_for, redirect, make_response, session
from mwproject import app
from mwproject.myforms import ContactForm

@app.route('/aboutus')
def about():
    form = ContactForm()
    if request.method == 'GET':
        return render_template('sample.html', form=form)
    elif request.method== 'POST':
        #retrieve the data, then save in database, flash and redirect
        if form.validate_on_submit():
            name = request.form['name']
            flash('Form Submitted...')
            return render_template('sample.html', form=form)
        else:
            return "please fill the form again"
    else:
        return "Invalid Access", 403





@app.route('/myform')
def myform():
    return render_template('form.html')


@app.route('/getform', methods =['POST', 'GET'])
def receive_message():
    fullname = request.form['fullname']
    email =  request.form['email']
    message = request.form['message']

    #insert into database
    flash('message has been successfully sent!')

    return redirect('/form')

@app.route('/search')
def search():
    keyw = request.args.get('txtsearch', '')
    return keyw









@app.route('/test')
def test(username):
    if username == 'admin':
        flash('text')
        flash('successfully logged in')



        return render_template('index1.html', username = username)
     #   return redirect('/base')


@app.route('/login', methods=['POST','GET'])
def mylogin():
    if request.method == 'GET':
        return "<h2>I will display Form Here</h2>"
    elif request.method == 'POST':
        return "<h1>Retrieve Data Submitted</h1>"

@app.route('/demo.html')
def demo():
    return 'hello'




@app.route('/blog')
def showblog():
    return render_template('index1.html') 

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('index1.html', error = "404: it appears you are here alone, the page you are looking for is gone"), 404


@app.errorhandler(500)
def internalerror(error):
    error = {'rude':"What do you want sef?", 'mild': "An Error Occured"}
    return render_template('index1.html', error=error), 404




@app.route('/dashboard/<user>')
def dashboard(user):
    return 'This is my dashboard' +user

@app.route('/admin/<usertype>/<userid>')
def admin(usertype,userid):
    return f"Welcome {usertype}, Your id is {userid}"

@app.route('/checkout', methods = ['POST','GET'])
def checkout():
    user ='ken'
    resp = make_response(render_template(products.html))
    resp.set_cookie('userID' user)
    return resp

@app.route('/visit')
def visit():
    if 'counnter' in session:
        session['counter'] = session['counter'] + 1
    else:
        session['counter'] = 1
   # session['category']= 'kids'
    cc = session['counter']
    return 'you have visited us' + str(cc) + 'times'


@app.route('/checkout')
def checkout():
    cat = session['category']
    return cat

