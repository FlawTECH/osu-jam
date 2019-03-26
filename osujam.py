import argparse
import sys
import os
from shutil import copyfile

parser = argparse.ArgumentParser(description='Extracts songs from the game osu! and copies them over to your preferred folder.')
parser.add_argument('-o', '--osu-src', help='root folder in which osu! is installed', required=True)
parser.add_argument('-d', '--dest', help='folder in which the files will be copied into', required=True)
args = parser.parse_args()

# get full path to audio file of song
def get_audio_path(song_dir):
    for file in os.listdir(song_dir):
        if file.endswith('.osu'):
            with open(os.path.join(song_dir, file), 'r', encoding='utf8') as f:
                for line in f:
                    if line.startswith('AudioFilename'):
                        song_file = os.path.join(song_dir, line[(15 if line[14]==' ' else 14):].rstrip())
                        if not os.path.isfile(song_file):
                            break
                        return song_file
    return ''

# populate a list of audio files to copy
def make_list(src):
    if not os.path.exists(src) or not os.path.isfile(os.path.join(src, 'osu!.exe')):
        print('Error: the folder you specified doesn\'t seem to be your osu! installation. '+
            'Make sure that you\'re pointing to the root of your osu! installation and try again.', file=sys.stderr)
    songs_dir = 'Songs'
    real_path = os.path.join(src, songs_dir)

    songs = []
    for dir in os.listdir(real_path):
        song_dir = os.path.join(real_path, dir)
        if(os.path.isdir(song_dir)):
            song_path = get_audio_path(song_dir)
            if len(song_path) > 0:
                songs.append(song_path)
    return songs

# transform filenames into actual song names based on parent folder
def normalize_filename(file):
    ext = os.path.splitext(file)[1]
    filename = os.path.split(os.path.split(file)[0])[1]+ext
    first_word = filename.split(' ', 1)[0]
    if first_word.isdigit():
        filename = filename[len(first_word)+1:]
    return filename

# copy files from osu! to chosen directory
def copy_files(files, dst):
    for file in files:
        filename = normalize_filename(file)
        print(os.path.join('Copying {0} ...'.format(filename)))
        try:
            copyfile(file, os.path.join(dst, filename))
        except OSError as err:
            print('Error: {0}'.format(err), file=sys.stderr)
    
if __name__ == '__main__':
    print(args.osu_src + ' ===> '+ args.dest)
    print('Checking for audio files (this may take a while depending on the amount of songs you have) ...')
    songs = make_list(args.osu_src)
    print('Found '+str(len(songs))+' songs. Copying ...')
    copy_files(songs, args.dest)
    print('Done !')