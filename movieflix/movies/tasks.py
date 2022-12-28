import subprocess
import os
from django.conf import settings

def convert_720p(source):    
    new_file_name =  source + '_720p.mp4'   
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, new_file_name)   
    subprocess.run(cmd)

def convert480p(source):
    ext = source.rsplit('\x5c', 1)[0]
    path = ext + '\x5c'
    input_ending = source.split('\x5c')[-1]
    output_ending = input_ending.split('.')[0] + '_480p.mp4'

    input_path = path + input_ending
    output_path = path + output_ending

    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(input_path, output_path) 
    subprocess.run(cmd, capture_output=True)
