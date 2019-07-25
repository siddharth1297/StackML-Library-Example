from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def image_classification():
    return render_template('index.html')

@app.route('/l1')
def face_emoji():
    return render_template('face-emoji.html')

@app.route('/l2')
def face_censor_emoji():
    return render_template('face-censor-emoji.html')

@app.route('/l3')
def face_expression_emoji():
    return render_template('face-expression-emoji.html')

if __name__ == '__main__':
    app.run(debug=True)