import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Response

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'server', 'uploads')
SHARED_FOLDER = os.path.join(os.getcwd(), 'server', 'shared')
MEDIA_FOLDER = os.path.join(os.getcwd(), 'server', 'media')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SHARED_FOLDER'] = SHARED_FOLDER
app.config['MEDIA_FOLDER'] = MEDIA_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2000 * 1024 * 1024  # 2 GB

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['SHARED_FOLDER']):
    os.makedirs(app.config['SHARED_FOLDER'])

if not os.path.exists(app.config['MEDIA_FOLDER']):
    os.makedirs(app.config['MEDIA_FOLDER'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'files' not in request.files:
            return redirect(request.url)
        files = request.files.getlist('files')
        for file in files:
            if file.filename == '':
                continue
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('list_files'))
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/uploads')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('files.html', files=files)


@app.route('/shared/<filename>')
def download_shared_file(filename):
    return send_from_directory(app.config['SHARED_FOLDER'], filename)


@app.route('/shared')
def list_shared_files():
    files = os.listdir(app.config['SHARED_FOLDER'])
    return render_template('shared_files.html', files=files)


@app.route('/media/<filename>')
def stream_media_file(filename):
    def generate():
        with open(os.path.join(app.config['MEDIA_FOLDER'], filename), 'rb') as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)
    return Response(generate(), mimetype='video/mp4')


@app.route('/media')
def list_media_files():
    files = os.listdir(app.config['MEDIA_FOLDER'])
    return render_template('media_files.html', files=files)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7878)
