import os
import argparse

def get_file_list(img_dir):
    file_list = os.listdir(img_dir)
    file_list = [f.split('.')[0] for f in file_list]
    return file_list

def gen_file(out_dir, img_dir, file_list):
    file_name = img_dir.split('/')[-1]
    file_path = os.path.join(out_dir, file_name)
    file_list = sorted(file_list)
    with open(file_path, "w") as f:
        [f.write(item+'\n') for item in file_list]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate file list from image dir")
    parser.add_argument('img_dir', help="image directory")
    parser.add_argument('out_dir', help="file list directory")

    args = parser.parse_args()

    file_list = get_file_list(args.img_dir)
    gen_file(args.out_dir, args.img_dir, file_list)