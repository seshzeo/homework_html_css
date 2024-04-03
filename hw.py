from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/robot.txt")
# def robot():
#     return redirect(url_for('static', filename='robot.txt'))

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
    # app.run('0.0.0.0', debug=False, ssl_context='adhoc')