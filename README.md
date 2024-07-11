<h2>Project Overview</h2><p>This project is a Flask web application designed to handle file uploads, downloads, and media streaming. The application organizes files into three categories: uploads, shared files, and media files. Users can upload files via a web interface, view lists of uploaded files, download shared files, and stream media files.</p><h2>Project Structure</h2><pre><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-vbnet">project/
│
├── server/
│   ├── uploads/
│   ├── <span class="hljs-keyword">shared</span>/
│   ├── media/
│
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── files.html
│   ├── shared_files.html
│   ├── media_files.html
|
├── static
│   ├── style.css
|
├── app.py
├── requirements.txt
└── README.md
</code></div></div></pre><h3>Directories</h3><ul><li><code>server/uploads</code>: Directory to store uploaded files.</li><li><code>server/shared</code>: Directory to store shared files.</li><li><code>server/media</code>: Directory to store media files.</li></ul><h3>Templates</h3><ul><li><code>index.html</code>: Main landing page.</li><li><code>upload.html</code>: Page for uploading files.</li><li><code>files.html</code>: Page to list uploaded files.</li><li><code>shared_files.html</code>: Page to list shared files.</li><li><code>media_files.html</code>: Page to list media files.</li></ul><h2>Setting Up the Project</h2><h3>Prerequisites</h3><ul><li>Python 3.x</li><li>Flask</li></ul><h3>Installation</h3><ol><li><p>Clone the repository:</p><pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git <span class="hljs-built_in">clone</span> https://github.com/mehdihoore/PyLocalUploadServer.git
<span class="hljs-built_in">cd</span> PyLocalUploadServer
</code></div></div></pre></li><li><p>Create and activate a virtual environment:</p><pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python -m venv venv
<span class="hljs-built_in">source</span> venv/bin/activate  <span class="hljs-comment"># On Windows use `venv\Scripts\activate`</span>
</code></div></div></pre></li><li><p>Install the required packages:</p><pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
</code></div></div></pre></li></ol><h3>Running the Application</h3><ol><li><p>Ensure the necessary directories exist:</p><pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python -c <span class="hljs-string">"import os; [os.makedirs(os.path.join(os.getcwd(), 'server', folder), exist_ok=True) for folder in ['uploads', 'shared', 'media']]"</span>
</code></div></div></pre></li><li><p>Start the Flask application:</p><pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python app.py
</code></div></div></pre></li><li><p>Open your web browser and go to <code>http://0.0.0.0:7878</code>.</p></li></ol><h2>Application Routes</h2><ul><li><code>/</code>: Main landing page, rendering <code>index.html</code>.</li><li><code>/upload</code>: Page for uploading files. Accepts <code>GET</code> and <code>POST</code> methods.</li><li><code>/uploads/&lt;filename&gt;</code>: Route to download a specific uploaded file.</li><li><code>/uploads</code>: Page to list all uploaded files.</li><li><code>/shared/&lt;filename&gt;</code>: Route to download a specific shared file.</li><li><code>/shared</code>: Page to list all shared files.</li><li><code>/media/&lt;filename&gt;</code>: Route to stream a specific media file.</li><li><code>/media</code>: Page to list all media files.</li></ul><h2>How to Use</h2><h3>Uploading Files</h3><ol><li>Navigate to the upload page by clicking the "Upload" link on the main page.</li><li>Select files to upload.</li><li>Click the "Upload" button to upload the selected files.</li><li>After uploading, you will be redirected to the list of uploaded files.</li></ol><h3>Viewing Uploaded Files</h3><ol><li>Navigate to the uploads page by clicking the "Uploads" link on the main page.</li><li>View the list of uploaded files. Click on any file to download it.</li></ol><h3>Downloading Shared Files</h3><ol><li>Navigate to the shared files page by clicking the "Shared Files" link on the main page.</li><li>View the list of shared files. Click on any file to download it.</li></ol><h3>Streaming Media Files</h3><ol><li>Navigate to the media files page by clicking the "Media Files" link on the main page.</li><li>View the list of media files. Click on any file to stream it directly in your browser.</li></ol><h2>Additional Information</h2><ul><li>The maximum upload file size is set to 2 GB.</li><li>The application runs on <code>http://0.0.0.0:7878</code>.</li></ul>
