from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Define route for home page
@app.route('/')
def home():
    # Get the list of files in the uploads directory
    files = os.listdir('static/uploads')
    return render_template('index.html', files=files)

# Define route for file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    file = request.files['file']
    # Generate a unique filename
    filename = file.filename
    i = 0
    while os.path.exists(f'static/uploads/{filename}'):
        i += 1
        filename = f"{os.path.splitext(file.filename)[0]}_{i}{os.path.splitext(file.filename)[1]}"
    # Save the uploaded file
    file.save(f'static/uploads/{filename}')
    return "File uploaded successfully!"

# Define route for file download
@app.route('/download/<filename>')
def download(filename):
    # Send the requested file to the user
    return send_from_directory('static/uploads', filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
