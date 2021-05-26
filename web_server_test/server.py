from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

# @app.route('/')
# def hello_world():
#     # return 'Hello, Mr.Chandrashekar!'
#     return  render_template('index.html')

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    # return 'Hello, Mr.Chandrashekar!'
    return  render_template('index.html', name=username, post_id=post_id)

@app.route('/about')
def about():
    # return 'Hello, Mr.Chandrashekar!'
    return  render_template('about.html')


@app.route('/blog')
def blog():
    return 'These are thoughts on blogs'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'