from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')  #we are replacing 'hello, mundo' with render_template
    #to link the index.html documenet since render_template lookis in the
    #templages folder first, we had to create one and move index.html

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
   with open('database.txt', mode='a') as database:
     email= data['email']
     subject = data['subject']
     message = data['message']
     file = database.write(f'\n{email}, {subject}, {message}')


@app.route('/pikapika.ico')
def icon():
    return 'hello'

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      data = request.form.to_dict()
      write_to_file(data)
      return redirect('/thankyou.html')
    else:
      return 'something went wrong, try again!'
