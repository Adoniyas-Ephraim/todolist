from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = '4u-Pi_aCa&L&0=WApiFr'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)