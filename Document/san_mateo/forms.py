from flask import forms

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])