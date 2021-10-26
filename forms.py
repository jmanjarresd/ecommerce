from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired, Email, Length

####################################################### USERS FORMS #######################################################
class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid name")])
    username = StringField('username', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid username")])
    password = PasswordField('password', validators=[DataRequired(message="You must fill this field"), Length(min=8, max=64, message="The password must contain a minimum of 8 characters")])
    email = StringField('email', validators=[DataRequired(message="You must fill this field"), Email()])
    phone = StringField('phone', validators=[DataRequired(message="You must fill this field"), Length(max=11, message="Enter a valid phone")])
    country = StringField('country', validators=[DataRequired(message="You must fill this field"), Length(max=64, message="Enter a valid country")])
    terms = BooleanField('terms', validators=[DataRequired()])
    submit = SubmitField('signUp')

class UpdateUserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid name")])
    username = StringField('username', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid username")])
    password = PasswordField('password', validators=[DataRequired(message="You must fill this field"), Length(min=8, max=64, message="The password must contain a minimum of 8 characters")])
    email = StringField('email', validators=[DataRequired(message="You must fill this field"), Email()])
    phone = StringField('phone', validators=[DataRequired(message="You must fill this field"), Length(max=11, message="Enter a valid phone")])
    country = StringField('country', validators=[DataRequired(message="You must fill this field"), Length(max=64, message="Enter a valid country")])
    submit = SubmitField('EDIT USER')
####################################################### USERS FORMS #######################################################

##################################################### PRDUCTS FORMS ######################################################
class AddProductForm(FlaskForm):
    product_name = StringField('product_name', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid name")])
    category = StringField('category', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid category")])
    code = StringField('code', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid code")])
    price = StringField('price', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid price")])
    product_description = TextAreaField('product_desription', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid description")])
    img = FileField('file')
    submit = SubmitField('addProduct')

class UpdateProductForm(FlaskForm):
    product_name = StringField('product_name', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid name")])
    category = StringField('category', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid category")])
    code = StringField('code', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid code")])
    price = StringField('price', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid price")])
    product_description = TextAreaField('product_desription', validators=[DataRequired(message="You must fill this field"), Length(min=5, max=64, message="Enter a valid description")])
    submit = SubmitField('addProduct')
##################################################### PRDUCTS FORMS ######################################################

####################################################### LOGIN FORM #######################################################
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message="You must fill this field"), Length(max=64)])
    password = PasswordField('password', validators=[DataRequired(message="You must fill this field"), Length(min=8 ,max=64, message="The password must contain a minimum of 8 characters")])
    remember = BooleanField('remember')
    submit = SubmitField('LOGIN')
####################################################### LOGIN FORM #######################################################