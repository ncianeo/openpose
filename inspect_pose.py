import subprocess
from multiprocessing import Pool
from os import listdir, walk, makedirs
from os.path import join, isfile, basename, isdir
import sys


"""
    키포인트 디텍션
    argv[1]: 이미지 저장 경로

    데이터 정리가 1차적으로 끝난 png 파일들에 대해서(최하위 레이어만) 키포인트 디텍션을 실행해 키포인트 값들을 json형식으로 저장함.
    이 파일을 실행하기 위해서는 openpose를 빌드해야함
"""
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
