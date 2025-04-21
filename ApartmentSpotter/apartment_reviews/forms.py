from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField, 
    TextAreaField, SelectField, FloatField, IntegerField,
    DecimalField, HiddenField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, NumberRange, 
    ValidationError, Optional
)

class LoginForm(FlaskForm):
    """User login form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    """User registration form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    user_type = SelectField('Account Type', choices=[
        ('tenant', 'Tenant'), 
        ('landlord', 'Landlord')
    ], validators=[DataRequired()])
    submit = SubmitField('Register')

class VerificationRequestForm(FlaskForm):
    """Form for tenants to request verification"""
    submit = SubmitField('Request Verification')

class ApartmentForm(FlaskForm):
    """Form for landlords to create apartment listings"""
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired(), Length(max=200)])
    city = StringField('City', validators=[DataRequired(), Length(max=100)])
    state = SelectField('Region', validators=[DataRequired()], choices=[
        ('POS', 'Port of Spain'), ('SAN', 'San Fernando'), ('ARI', 'Arima'),
        ('CHA', 'Chaguanas'), ('PTF', 'Point Fortin'), ('DMA', 'Diego Martin'),
        ('TUP', 'Tunapuna-Piarco'), ('PED', 'Penal-Debe'), ('COV', 'Couva-Tabaquite-Talparo'),
        ('SJL', 'San Juan-Laventille'), ('RCL', 'Rio Claro-Mayaro'), ('SIP', 'Siparia'),
        ('PRI', 'Princes Town'), ('SGE', 'Sangre Grande'), ('TOB', 'Tobago')
    ])
    zip_code = StringField('Postal Code', validators=[DataRequired(), Length(max=10)])
    price = FloatField('Monthly Rent (TTD)', validators=[
        DataRequired(),
        NumberRange(min=0, message='Price must be positive')
    ])
    bedrooms = IntegerField('Bedrooms', validators=[
        DataRequired(),
        NumberRange(min=0, message='Number of bedrooms must be positive')
    ])
    bathrooms = DecimalField('Bathrooms', validators=[
        DataRequired(),
        NumberRange(min=0, message='Number of bathrooms must be positive')
    ])
    amenities = TextAreaField('Amenities (comma-separated)', validators=[DataRequired()])
    submit = SubmitField('Create Listing')

class ReviewForm(FlaskForm):
    """Form for tenants to review apartments"""
    rating = IntegerField('Rating (1-5)', validators=[
        DataRequired(),
        NumberRange(min=1, max=5, message='Rating must be between 1 and 5')
    ])
    comment = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit Review')

class SearchForm(FlaskForm):
    """Basic search form for homepage"""
    query = StringField('Search by city, region, or postal code', validators=[DataRequired()])
    submit = SubmitField('Search')

class ApartmentSearchForm(FlaskForm):
    """Advanced search form for filtering apartment listings"""
    city = StringField('City', validators=[Optional()])
    state = SelectField('Region', validators=[Optional()], choices=[
        ('', 'Any Region'),
        ('POS', 'Port of Spain'), ('SAN', 'San Fernando'), ('ARI', 'Arima'),
        ('CHA', 'Chaguanas'), ('PTF', 'Point Fortin'), ('DMA', 'Diego Martin'),
        ('TUP', 'Tunapuna-Piarco'), ('PED', 'Penal-Debe'), ('COV', 'Couva-Tabaquite-Talparo'),
        ('SJL', 'San Juan-Laventille'), ('RCL', 'Rio Claro-Mayaro'), ('SIP', 'Siparia'),
        ('PRI', 'Princes Town'), ('SGE', 'Sangre Grande'), ('TOB', 'Tobago')
    ])
    min_price = FloatField('Min Price (TTD)', validators=[Optional()])
    max_price = FloatField('Max Price (TTD)', validators=[Optional()])
    bedrooms = SelectField('Bedrooms', validators=[Optional()], choices=[
        ('', 'Any'),
        ('0', 'Studio'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4+')
    ], coerce=lambda x: x or None)
    bathrooms = SelectField('Bathrooms', validators=[Optional()], choices=[
        ('', 'Any'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3+')
    ], coerce=lambda x: x or None)
    submit = SubmitField('Search')
