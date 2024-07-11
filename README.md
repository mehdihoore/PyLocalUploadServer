
Read Me
Project Overview
This project is a Flask web application designed to handle file uploads, downloads, and media streaming. The application organizes files into three categories: uploads, shared files, and media files. Users can upload files via a web interface, view lists of uploaded files, download shared files, and stream media files.

Project Structure
vbnet
Copy code
project/
│
├── server/
│   ├── uploads/
│   ├── shared/
│   ├── media/
│
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── files.html
│   ├── shared_files.html
│   ├── media_files.html
│
├── app.py
├── requirements.txt
└── README.md
Directories
server/uploads: Directory to store uploaded files.
server/shared: Directory to store shared files.
server/media: Directory to store media files.
Templates
index.html: Main landing page.
upload.html: Page for uploading files.
files.html: Page to list uploaded files.
shared_files.html: Page to list shared files.
media_files.html: Page to list media files.
Setting Up the Project
Prerequisites
Python 3.x
Flask
Installation
Clone the repository:

bash
Copy code
git clone github.com/mehdihoore/PyLocalUploadServer.git
cd project
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Running the Application
Ensure the necessary directories exist:

bash
Copy code
python -c "import os; [os.makedirs(os.path.join(os.getcwd(), 'server', folder), exist_ok=True) for folder in ['uploads', 'shared', 'media']]"
Start the Flask application:

bash
Copy code
python app.py
Open your web browser and go to http://0.0.0.0:7878.

Application Routes
/: Main landing page, rendering index.html.
/upload: Page for uploading files. Accepts GET and POST methods.
/uploads/<filename>: Route to download a specific uploaded file.
/uploads: Page to list all uploaded files.
/shared/<filename>: Route to download a specific shared file.
/shared: Page to list all shared files.
/media/<filename>: Route to stream a specific media file.
/media: Page to list all media files.
How to Use
Uploading Files
Navigate to the upload page by clicking the "Upload" link on the main page.
Select files to upload.
Click the "Upload" button to upload the selected files.
After uploading, you will be redirected to the list of uploaded files.
Viewing Uploaded Files
Navigate to the uploads page by clicking the "Uploads" link on the main page.
View the list of uploaded files. Click on any file to download it.
Downloading Shared Files
Navigate to the shared files page by clicking the "Shared Files" link on the main page.
View the list of shared files. Click on any file to download it.
Streaming Media Files
Navigate to the media files page by clicking the "Media Files" link on the main page.
View the list of media files. Click on any file to stream it directly in your browser.
Additional Information
The maximum upload file size is set to 2 GB.
The application runs on http://0.0.0.0:7878.
