import subprocess
from multiprocessing import Pool
from os import listdir, walk, makedirs
from os.path import join, isfile, basename, isdir
import sys


def inspect_path(img_path):
    json_path = join(*img_path.split("/")[-4:-2])
    print(img_path)
    if not isdir(json_path):
        try:
            makedirs(json_path)
        except:
            pass
    if not isfile(join(json_path, basename(img_path).replace(".png", "_keypoints.json"))):
        return subprocess.run("./build/examples/tutorial_api_cpp/03_keypoints_from_image.bin --image_path \"{}\" --write_json \"{}\" --no-display".format(img_path, json_path), shell=True, check=True)
    else:
        return None


base_path = sys.argv[1]
img_paths = []
for p, d, f in walk(base_path):
    if p.endswith("process 0"):
        for fn in f:
            if fn.endswith(".png"):
                img_paths.append(join(p, fn))


if __name__ == "__main__":
    pool = Pool()
    print(list(pool.map(inspect_path, img_paths)))
