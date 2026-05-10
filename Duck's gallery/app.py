import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = os.path.join('static', 'images')
    # This line checks if the filename is NOT 'duck_logo.png'
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(('png', 'jpg', 'jpeg', 'gif')) and img != 'duck_logo.png']
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)