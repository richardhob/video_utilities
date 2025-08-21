
import os
import pathlib
import argparse
import subprocess

def do(title, indicies, link):
    idx = ','.join(map(str, indicies))
    p = subprocess.run(f"yt-dlp -I {idx} -o \"{title}E%(playlist_index)03d.old.%(ext)s\" {link}", shell=True)

def get_rename(name, extension, indicies):
    values = []
    for i, index in enumerate(indicies, 1):
        old = f"{name}E{index:03d}.old.{extension}"
        new = f"{name}E{i:03d}.{extension}"
        values.append((old, new))

    return values

def rename(values):
    for old, new in values:
        try:
            os.rename(old, new)
        except:
            pass

def fix(name, extension, indicies):
    values = []
    for index in indicies:
        old = f"{name}E{index:04d}.old.{extension}"
        new = f"{name}E{index:03d}.old.{extension}"
        values.append((old, new))

    return values

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("name", help="File Name Prefix")
    parser.add_argument("link", help="Link to the YT Playlist")
    parser.add_argument("--path", help="Path to the directory to save things to", default=pathlib.Path("."), type=pathlib.Path)
    parser.add_argument("--renameOnly", help="Skip downloading, rename only", action="store_true", default=False)
    parser.add_argument("--extension", help='Video file extension (of download file for renaming)', default='mp4')
    parser.add_argument("--fix", help='Quick fix for movies (Remove)', default=False, action='store_true')
    parser.add_argument("-x", help='Force the rename', action="store_true", default=False)
    parser.add_argument("indicies", help="YT Playlist indicies to download", nargs="+", type=int)

    args = parser.parse_args()

    if args.fix:
        values = fix(args.name, args.extension, args.indicies)
        if args.x == True:
            rename(values)
        else:
            for (old, new) in values:
                print(f"{old} -> {new}")

        return

    if args.renameOnly == False:
        do(args.name, args.indicies, args.link)

    values = get_rename(args.name, args.extension, args.indicies)

    if args.x == True:
        rename(values)
    else:
        for (old, new) in values:
            print(f"{old} -> {new}")

if __name__ == '__main__':
    main()
