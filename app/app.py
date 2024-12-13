from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    css_file_path = os.path.join(app.static_folder, 'css/home.css')
    css_last_modified = int(os.path.getmtime(css_file_path))
    return render_template('home.html', css_last_modified=css_last_modified)

@app.route("/projects")
def projects():
    css_file_path = os.path.join(app.static_folder, 'css/styles.css')
    css_last_modified = int(os.path.getmtime(css_file_path))
    return render_template("projects.html", css_last_modified=css_last_modified)

@app.route("/contact")
def contact():
    css_file_path = os.path.join(app.static_folder, 'css/styles.css')
    css_last_modified = int(os.path.getmtime(css_file_path))
    return render_template("contact.html", css_last_modified=css_last_modified)

@app.route("/about")
def about():
    css_file_path = os.path.join(app.static_folder, 'css/styles.css')
    css_last_modified = int(os.path.getmtime(css_file_path))
    return render_template("about.html", css_last_modified=css_last_modified)

@app.route('/gallery')
def gallery():
    css_file_path = os.path.join(app.static_folder, 'css/gallery.css')
    css_last_modified = int(os.path.getmtime(css_file_path))
    image_folder = os.path.join(app.static_folder, 'assets/gallery/')
    images = [f"assets/gallery/{file}" for file in os.listdir(image_folder) if file.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('gallery.html', css_last_modified=css_last_modified, images=images)


if __name__ == '__main__':
    app.run(debug=True)
