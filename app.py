from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news4')
def news4():
    return render_template('news4.html')

@app.route('/news4_2')
def news4_2():
    return render_template('news4_2.html')

@app.route('/gk')
def gk():
    return render_template('gk.html')

if __name__ == '__main__':
    app.run(debug=True)

# Required for Vercel
app.debug = True