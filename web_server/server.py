from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

print(__name__)


@app.route('/')
def my_home():
    # return 'Hello, Mr.Chandrashekar!'
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
        	return 'did not save to database'
    else:
        return 'something went wrong'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(database2, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])

# @app.route('/about.html')
# def about():
#     # return 'Hello, Mr.Chandrashekar!'
#     return  render_template('about.html')

# # @app.route('/')
# # def my_home():
# #     # return 'Hello, Mr.Chandrashekar!'
# #     return render_template('index.html')


# @app.route('/works.html')
# def works():
#     # return 'Hello, Mr.Chandrashekar!'
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     # return 'Hello, Mr.Chandrashekar!'
#     return render_template('contact.html')
