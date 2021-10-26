from flask import Flask, render_template, request, flash, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from forms import LoginForm, SignupForm, UpdateProductForm, UpdateUserForm ,AddProductForm
import controller
import datetime
import os

app=Flask(__name__)

#settings
app.secret_key = 'my_secret_key'

UPLOAD_FOLDER = os.path.abspath("static/images/")
ALLOWED_EXTENSIONS = set(['png','jpg','jpge'])

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):

    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

#############Definición de rutas#######################

# START CRUD PRODUCTS #
"""Home"""
@app.route('/')
def Index():
    data = controller.get_Products()
    users_sessions = session
    print(users_sessions)
    return render_template('home.html', prods = data, users_sessions = users_sessions )

"""Add product"""
@app.route('/add_product')
def add_product():
    if 'superadmin' in session or 'admin'in session:
        form = AddProductForm()
        return render_template('Add.html', form = form)
    else:
        return redirect('/')

@app.route('/agg-product', methods=['POST'])
def add_prod():
    form = AddProductForm()
    if request.method == 'POST' and form.validate_on_submit() and 'superadmin' in session or 'admin'in session:
        product_name = form.product_name.data
        category = form.category.data
        code = form.code.data
        price = form.price.data
        product_description = form.product_description.data
        if 'img' not in request.files:
            return "<h1>The form has no file part</h1>"
        img = form.img.data
        if img.filename == "":
            return "<h1>No file selected</h1>"
        if img and allowed_file(img.filename):
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            controller.agg_product(product_name, category, code, price, product_description, filename)
            return redirect('/products_page')
        return "<h1>File not allowed</h1>"
    else:
        return "<h1>Error. You do not have permission to access this page</h1>"

"""Edit Products"""
@app.route('/edit_product/<id>')
def edit_product(id):
    if 'superadmin' in session:
        form = AddProductForm()
        data = controller.edit_Products(id)
        form.product_name.data = data[1]
        form.category.data = data[2]
        form.code.data = data[3]
        form.price.data = data[4]
        form.product_description.data = data[5]
        return render_template('Edit.html', ids = data, form = form)
    else:
        return redirect('/')

@app.route('/update_product/<id>', methods=['POST'])
def update_product(id):
    form = UpdateProductForm()
    if request.method == 'POST' and form.validate_on_submit() and 'superadmin' in session:
        product_name = form.product_name.data
        category = form.category.data
        code = form.code.data
        price = form.price.data
        product_description = form.product_description.data
        controller.update_products(product_name, category, code, price, product_description, id)

        return redirect('/products_page')
    else:
        return "<h1>Error. You do not have permission to access this page</h1>"

"""Delete Products"""
@app.route('/delete_product/<id>')
def delete_product(id):
    if 'superadmin' in session:
        data = controller.edit_Products(id)
        os.remove("static/images/" + data[6])
        controller.delete_products(id)
        return redirect('/products_page')
    else:
        return "<h1>Error. You do not have permission to access this page</h1>"
# FINAL CRUD PRODUCTS #

# START CRUD USERS #

"""Sign up"""
@app.route('/sign-up')
def sign_up():
        form = SignupForm()
        return render_template('Sign-up.html', form = form)

"""Add Users"""
@app.route('/agg-user', methods=['POST'])
def add_user():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = generate_password_hash(form.password.data)
        email = form.email.data
        phone = form.phone.data
        country = form.country.data
        date = str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year) + " - " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
        controller.agg_user(name, username, password, email, phone, country, date)

        return redirect('/sign-in')
    else:
        return "<h1>Error. You do not have permission to access this page</h1>"

"""Edit Users"""
@app.route('/edit_user/<id>')
def edit_user(id):
    if 'superadmin' in session or 'admin'in session:
        form = SignupForm()
        data = controller.edit_users(id)
        form.name.data = data[1]
        form.username.data = data[2]
        form.password.data = data[3]
        form.email.data = data[4]
        form.phone.data = data[5]
        form.country.data = data[6]
        return render_template('edit_users.html', user_ids = data, form = form)
    else:
        return redirect('/')

@app.route('/update_user/<id>', methods=['POST'])
def update_user(id):
    form = UpdateUserForm()
    if request.method == 'POST' and form.validate_on_submit() and 'superadmin' in session or 'admin'in session:
        name = form.name.data
        username = form.username.data
        password = generate_password_hash(form.password.data)
        email = form.email.data
        phone = form.phone.data
        country = form.country.data
        date = str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year) + " - " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
        controller.update_users(name, username, password, email, phone, country, date, id)

        return redirect('/users_page')
    else:
        return "<h1>Error. You do not have permission to access this page</h1>"
    

"""Delete Users"""
@app.route('/delete_user/<id>')
def delete_user(id):
    if 'superadmin' in session or 'admin'in session:
        controller.delete_users(id)

        return redirect('/users_page')
    else:
        return "<h1>Error. You do not have permission to access this page</h1>"

# FINAL CRUD USERS #

"""Sign in"""
@app.route('/sign-in')
def sign_in():
    form = LoginForm()
    return render_template('Sign-in.html', form = form)

@app.route('/login', methods=['POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = controller.login_users(username)
        admin = controller.login_admins(username)
        if user is not None:
            if len(user)>0 and check_password_hash(user[3], password):
                session['user'] = username
                return redirect('/')
        if admin is not None:
            if len(admin)>0 and check_password_hash(admin[4], password) and admin[1] == 'superadmin':
                session['superadmin'] = username
                print(session)
                return redirect('/')
            if len(admin)>0 and check_password_hash(admin[4], password) and admin[1] == 'admin':
                session['admin'] = username
                print(session)
                return redirect('/')
    return redirect('/sign-in')

@app.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect('/')

"""Details products"""
@app.route('/product/<id>')
def products(id):
    if 'superadmin' in session or 'admin'in session or 'user' in session:
        data = controller.edit_Products(id)
        return render_template('Details-products.html', prod = data)
    else:
        return "<h1>You must login to view this page"

"""Wish List"""
@app.route('/wish-list')
def wish_list():
    if 'superadmin' in session or 'admin'in session or 'user' in session:
        data = controller.get_Products()
        return render_template('Wish-list.html', prod = data)
    else:
        return redirect('/')

"""Dashboard"""
@app.route('/dashboard')
def dashboard():
    if 'superadmin' in session or 'admin'in session:
        return render_template('Dashboard.html')
    else:
        return redirect('/')

@app.route('/users_page')
def users_page():
    if 'superadmin' in session or 'admin'in session:
        data = controller.get_Users()
        users_sessions = session
        print(users_sessions)
        return render_template('users_page.html', users = data, users_sessions = users_sessions)
    else:
        return redirect('/')

@app.route('/products_page')
def products_page():
    if 'superadmin' in session or 'admin'in session:
        data = controller.get_Products()
        return render_template('products_page.html', products = data)
    else:
        return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Page not found</h1>', 404

""" #Inciar servidor
if __name__=='__main__':
    app.run(port=3000, debug = True) """

