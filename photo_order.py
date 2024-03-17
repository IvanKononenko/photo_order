import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

print(os.getcwd())
print(os.listdir())

creation_time = os.path.getctime('GOPR0351.JPG')
creation_date = datetime.fromtimestamp(creation_time)
print(creation_date.year)