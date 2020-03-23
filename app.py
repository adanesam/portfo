# To activate your vertual C:\Users\Adane\PycharmProjects\web-server>venv\Scripts\activate
# This file should be named app.py to activate our server. Took me a while
# once you are in vev, (venv) C:\Users\Adane\PycharmProjects\web-server>set FLASK_APP = app.py
# then (venv) C:\Users\Adane\PycharmProjects\web-server>flask run  'NOT run flask'
# If the 'Debug mode is off', you need to re-run flask every time you make a change
# To update our changes in real time, you need to turn on the Debug mode,
# set FLASK_ENV = development, instead of set FLASK_APP = app.py, then flask run


from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# print(__name__)


###################################################################################
@app.route('/')  # create a template folder, flask will look for index.html in this folder
def my_home():

    return render_template('index.html')


# Instead of copy and paste different route functions above, we can make it more dynamic

@app.route('/<page_name>')
def html_page(page_name):

    return render_template(page_name)

# Collecting data from users and save it in a database as a # TEXT file

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

# Collecting data from users and save it in a database as a # CSV file

def write_to_csv(data): # import and refer the csv module documentation
    with open('database.csv', newline='', mode = 'a') as database2: # write the headers in your csv database file
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data) # calling write_to_file data function # To use the csv database, change it to write to csv
            return redirect('/thankyou.html') # not working for now
        except:
            return 'did not save to database'
    else:
        return 'somthing went wrong, try again!'


##########################################################################################



# @app.route('/index.html')
# def home():
#
#     return render_template('index.html')
#
# @app.route('/about.html')
# def about():
#
#     return render_template('about.html')
#
# @app.route('/works.html')
# def works():
#
#     return render_template('works.html')
#
# @app.route('/templates/work.html')
# def work():
#
#     return render_template('work.html')
# @app.route('/contact.html')
# def contact():
#
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def component():
#
#     return render_template('components.html')
#
#
# @app.route('/works/discover.html')
# def discover():
#
#     return render_template('components.html')




# @app.route('/<username>') # The url will display the user name /username in the html web page
# #http://127.0.0.1:5000/adane = displays 'Hello adane!'
# def hello_world(username = None):
#
#     return 'Hello, {}!'.format(username)


# Let's create another routes or directory

# @app.route('/blog') # This displays the message with url= 'http://127.0.0.1:5000/blog'
# def blog():    # The function name should be unique, no repeatation
#
#     return 'I am a Web master!'
#
# @app.route('/blog/2020/dogs') # url = 'http://127.0.0.1:5000/blog'/2020/dogs
# def dogs():
#
#     return 'Hello doggy!'

# Can we now now run from files like html, css, js? Yes, using a module
# called render_template, import first

# @app.route('/render')  # create a template folder, flask will look for index.html in this folder
# def render():
#
#     return render_template('index.html')


# @app.route('/about')  # Creating differnent routes, url = http://127.0.0.1:5000/about
# def about():
#
#     return render_template('about.html')
#
# # Static files like css and js files need to be stored in a 'static' folder
# # Now change the file path in the main index.html file
#
# @app.route('/cssJs')  # Now, we modified the path to the css and js files in index.html in this folder
# def cssJs():
#
#     return render_template('index.html')
#
# # Adding favicon.ico, an icon that is displayed at tools bar when we access any website
# # goto the index.html file and add a link to this image. Find an image and save it in folder
#
