from werkzeug.utils import secure_filename
from .. import create_app
import os 
import cloudinary
from cloudinary import uploader
from pprint import pprint
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class FileUploader:

    def __init__(self, file):
        self.app = create_app()
        self.FILE = file
        self.ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
        self.app.config['UPLOAD_FOLDER'] = "./webapp/uploads/"
        cloudinary.config(
            cloud_name = os.environ.get("CLOUDINARY_CLOUDNAME"),  
            api_key = os.environ.get("CLOUDINARY_APIKEY"),  
            api_secret = os.environ.get("CLOUDINARY_APISECRET")  
        )
        self.isUploaded = False

    def isImage(self): 
        return '.' in self.FILE.filename and \
        self.FILE.filename.rsplit('.', 1)[1].lower() in self.ALLOWED_IMAGE_EXTENSIONS

    def uploadFile(self):
        self.secureName = secure_filename(self.FILE.filename)
        UPLOAD_PATH = os.path.join(self.app.config["UPLOAD_FOLDER"], self.secureName)
        self.FILE.save(UPLOAD_PATH)
        return UPLOAD_PATH

    def uploadToCloudinary(self):
        uploadedFile = uploader.upload(self.FILE, folder = "WeirdDiary/uploads")
        if uploadedFile:
            self.isUploaded = True
        pprint(uploadedFile)
        return uploadedFile['secure_url']

    @staticmethod
    def deleteFileFromCloudinary(publicid):
        uploader.destroy(public_id=publicid)
        