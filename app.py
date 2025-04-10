from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
import os
from PIL import Image
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'D:/engineer/projects_git/breast_cancer/static/uploaded'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = YOLO('best.pt')  # Load your model

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            filename = str(uuid.uuid4()) + '.png'
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)

            # Run detection
            results = model(filepath)

            # Save output image
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'pred_' + filename)
            results[0].save(filename=output_path)

            return render_template('index.html',
                                   original=url_for('static', filename='uploaded/' + filename),
                                   result=url_for('static', filename='uploaded/pred_' + filename))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)