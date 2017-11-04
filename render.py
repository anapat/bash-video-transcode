# -*- coding: utf-8 -*-
import os, subprocess

def render(source, destination):
    cmd = '/usr/bin/HandBrakeCLI -i %s -o %s -e x264 --cfr -q 16  -B 72 -X 720' % (source, destination)
    os.system(cmd)
    if os.path.isfile(destination):
        if os.stat(source).st_size  > os.stat(destination).st_size:
            os.system('rm  %s' % source)
            os.system('mv  %s %s' % (destination ,source))
        else:
            os.system('rm  %s' % destination)

def count_all_file():
    count = 0
    for path, subdirs, files in os.walk('.'):
        for name in files:
            if name not in os.path.basename(__file__):
                file_name , file_extension = os.path.splitext(name)
                if '.mp4' in file_extension.lower() and 'render' not in path:
                    count += 1
    return count

if __name__ == '__main__':
    count = 1
    count_all = count_all_file()
    for path, subdirs, files in os.walk('.'):
        for name in files:
            if name not in os.path.basename(__file__):
                file_name , file_extension = os.path.splitext(name)
                if '.mp4' in file_extension.lower() and 'render' not in path:
                    create_folder = os.path.join(path, 'render')
                    if not os.path.exists(create_folder):
                        os.makedirs(create_folder)
                    print '> Execute File (%s/%s) : %s '% (count, count_all, os.path.join(path, name)[1:])
                    source = os.path.join(path, file_name + file_extension)
                    destination = os.path.join(create_folder, file_name + file_extension)
                    render(source, destination)
                    count += 1
