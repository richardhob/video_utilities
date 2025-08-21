
import argparse 
from pathlib import Path

import natsort as ns

def rename(path, name, season, extension, make_change=False, start_value=1):
    found = []
    from_to = {}
    for some_file in path.iterdir():
        if some_file.suffix != extension:
            continue
        found.append(some_file)

    found = ns.natsorted(found)

    count = start_value
    for some_file in found:
        target = Path(path) / f"{name}_S{season:02}E{count:03}{extension}"

        if make_change:
            some_file.rename(target)
        else:
            print(f"{some_file} -> {target}")
        count += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("path")
    parser.add_argument("name")
    parser.add_argument("season", type=int)
    parser.add_argument("-s", type=int, default=1, help="Number to start at (default is 1)")
    parser.add_argument("-x", action="store_true")
    parser.add_argument("--extension", default='.m4v')

    args = parser.parse_args()
    rename(Path(args.path), args.name, args.season, args.extension, args.x, args.s)
