from flask import Flask, render_template, request, redirect
import csv

# In python there is complete built-in python module for csv files
# CSV: Comma Separated Values
# https://docs.python.org/3/library/csv.html

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


'''
@app.route('/works.html')
def my_work():
    return render_template('works.html')


@app.route('/contact.html')
def my_contact():
    return render_template('contact.html')


@app.route('/about.html')
def my_about():
    return render_template('about.html')


@app.route('/components.html')
def my_components():
    return render_template('components.html')
'''


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # convert form data into dictionary format
            write_to_csv(data)
            return redirect('/Thankyou.html')  # or we can use 'render_template('thank_you.html')'
        except:
            return 'Did not save to database'
    else:
        return 'Not Submitted'


def write_to_file(data):
    with open('database.txt', mode='a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    # now create csv writer object that dont need to create
    # when we write in txt file
    with open("./database.csv", mode='a', newline='') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
