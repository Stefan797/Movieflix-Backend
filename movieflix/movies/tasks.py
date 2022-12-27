import subprocess
import os
from django.conf import settings

def convert_720p(source):    
    new_file_name =  source + '_720p.mp4'   
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, new_file_name)   
    subprocess.run(cmd)

def convert480p(source):
    path = os.path.join(settings.MEDIA_ROOT, 'movie' )
    ext = source.rsplit('\x5c', 1)[0]
    final_path = ext + '\x5c'
    destination_path = ext + '_480p.mp4'
    new_path = source.split('\x5c')[-1]
    new_path2 = new_path.split('.')[0] + '_480p.mp4'
    print(final_path + new_path2)
    
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(final_path, final_path + new_path2)    
    run = subprocess.run(cmd, capture_output=True)
