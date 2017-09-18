import json
import os, shutil


def clear_dir(folder):
    try:
        shutil.rmtree(folder)
    except:
        pass
    os.makedirs(folder)

def make_folders(dest, folders):
    for folder in folders:
        os.makedirs(dest+os.sep+folder)

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

def copy_all(source, dest, tagged_clusters):
    for k, v in tagged_clusters.iteritems():
        for artist in v:
            try:
                copy_and_overwrite(source+os.sep+artist, dest+os.sep+k+os.sep+artist)
            except:
                print "can't copy", artist

if __name__ == '__main__':
    with open('tagged_clusters20.json', 'rb') as f:
        tagged_clusters = json.load(f)

    print tagged_clusters

    source_directory = 'C:\Users\\birdm\Desktop\Organized Artist'
    dest_directory = 'C:\Users\\birdm\Desktop\sorted_artists'

    clear_dir(dest_directory)
    make_folders(dest_directory, tagged_clusters.keys())
    print source_directory
    print dest_directory
    print tagged_clusters
    copy_all(source_directory, dest_directory, tagged_clusters)