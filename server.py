from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')  

@app.route('/about')
def about():
    return render_template('About.html')  

@app.route('/blog')
def blog():
    return 'Welcome to the blog page!'

@app.route('/blog2')  
def blog2():
    return 'my second blog!'

if __name__ == '__main__':
    app.run(debug=True) 