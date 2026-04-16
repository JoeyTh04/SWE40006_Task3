from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Task 3.1 Complete!</h1>
    <img src="/static/render.jpg" alt="Render Image" style="max-width: 100%;">
    '''

if __name__ == '__main__':
    app.run()