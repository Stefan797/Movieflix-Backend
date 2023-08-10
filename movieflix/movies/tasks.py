import subprocess
import os
from django.conf import settings

def convert_720p(source):    
    ext = source.rsplit('\x5c', 1)[0]
    # path = ext
    input_ending = source.split('\x5c')[-1]
    output_ending = input_ending.split('.')[0] + '_720p.mp4'

    input_path = input_ending
    output_path = output_ending
    cmd = ['ffmpeg', '-i', input_path, '-s', 'hd720', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', output_path]
    try:
        result = subprocess.run(cmd, capture_output=True)
        print('success', result.returncode)
        if result.returncode != 0:
            print('Error:', result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print("Fehler aufgetreten:")
        print(e.stderr.decode())

def convert_480p(source):
    ext = source.rsplit('\x5c', 1)[0]
    # path = ext
    input_ending = source.split('\x5c')[-1]
    output_ending = input_ending.split('.')[0] + '_480p.mp4'
    input_path = input_ending
    output_path = output_ending
    cmd = ['ffmpeg', '-i', input_path, '-s', 'hd480', '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', output_path]
    try:
        result = subprocess.run(cmd, capture_output=True)
        print('success', result.returncode)
        if result.returncode != 0:
            print('Error:', result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print("Fehler aufgetreten:")
        print(e.stderr.decode())


# Falls noch anders bei Windows

# def convert_720p(source):    
#     ext = source.rsplit('\x5c', 1)[0]
#     path = ext + '\x5c'
#     input_ending = source.split('\x5c')[-1]
#     output_ending = input_ending.split('.')[0] + '_720p.mp4'

#     input_path = path + input_ending
#     output_path = path + output_ending

#     cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(input_path, output_path) 
#     subprocess.run(cmd, capture_output=True)

# def convert_480p(source):
#     ext = source.rsplit('\x5c', 1)[0]
#     path = ext + '\x5c'
#     input_ending = source.split('\x5c')[-1]
#     output_ending = input_ending.split('.')[0] + '_480p.mp4'

#     input_path = path + input_ending
#     output_path = path + output_ending

#     cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(input_path, output_path) 
#     subprocess.run(cmd, capture_output=True)
