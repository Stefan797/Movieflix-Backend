import subprocess
import os
from django.conf import settings

def convert_720p(source):    
    new_file_name =  source + '_720p.mp4'   
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, new_file_name)   
    subprocess.run(cmd)

def convert480p(source):
    path = os.path.join(settings.MEDIA_ROOT, 'movie' )
    ext = source.split('.')[0]
    final_path = ext + '.mp4'
    destination_path = ext + '_480p.mp4'
    
    
    print(source)
    
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, destination_path)    
    subprocess.run(cmd, capture_output=True)
