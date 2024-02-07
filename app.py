# from flask import Flask, render_template
# from flask_minify import Minify

# app = Flask(__name__)

# # Enable minification
# Minify(app=app, html=True, js=True, cssless=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

if __name__ == '__main__':
    app.run(debug=True)







