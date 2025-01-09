from flask import Flask, render_template, redirect, url_for, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/get_images', methods=['GET'])
def get_images():
    image_paths = [
        'static/assets/gallery/01.png', 'static/assets/gallery/02.png', 'static/assets/gallery/03.png', 
        'static/assets/gallery/04.png', 'static/assets/gallery/05.png', 'static/assets/gallery/06.png', 
        'static/assets/gallery/07.png', 'static/assets/gallery/08.png', 'static/assets/gallery/09.png', 
        'static/assets/gallery/10.png', 'static/assets/gallery/11.png', 'static/assets/gallery/12.png', 
        'static/assets/gallery/13.png', 'static/assets/gallery/14.png', 'static/assets/gallery/15.png', 
        'static/assets/gallery/16.png', 'static/assets/gallery/17.png', 'static/assets/gallery/18.png', 
        'static/assets/gallery/19.png'
    ]

    return jsonify(image_paths)

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
    images = sorted(
        [
            f"assets/gallery/{file}" 
            for file in os.listdir(image_folder) 
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
        ]
    )
    
    print(images) 
    
    return render_template('gallery.html', css_last_modified=css_last_modified, images=images)


if __name__ == '__main__':
    app.run(debug=True)
