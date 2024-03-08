from flask import Flask, render_template
import requests

app = Flask(__name__)
age_url='https://api.agify.io/?name='
@app.route("/")
def home():
    return "<h1>Hello! Extend the url to '/guess/yourname' to find your age and gender!</h1>"

@app.route("/guess/<uname>")
def guess(uname):
    #Flask will look for templates in the "templates" folder.
    #All other files like CSS and JS will be looked in "static" folder.
    age_url=f'https://api.agify.io/?name={uname}'
    response_age = requests.get(age_url)
    age_data = response_age.json()
    age = age_data['age']

    gender_url = f'https://api.genderize.io/?name={uname}'
    response_gender = requests.get(gender_url)
    gender_data = response_gender.json()
    gender = gender_data['gender']

    return render_template("index.html", uname=uname, gender= gender, age= age)

if __name__ == '__main__':
    app.run(debug=True)