from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('land'))

@app.route('/land')
def land():
    css_file_path = os.path.join(app.static_folder, 'styles.css')
    css_last_modified = int(os.path.getmtime(css_file_path))
    return render_template('land.html', css_last_modified=css_last_modified)

if __name__ == '__main__':
    app.run(debug=True)
