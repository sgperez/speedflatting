from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def render_index(param = None):
	return render_template('main.html', param = param)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)