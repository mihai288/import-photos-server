from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.getcwd()

@app.route('/')
def upload_form():
    return render_template_string('''
        <form method="post" enctype="multipart/form-data" action="/upload">
            <input type="file" name="file">
            <button type="submit">Upload</button>
        </form>
    ''')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return f"File {file.filename} uploaded successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
