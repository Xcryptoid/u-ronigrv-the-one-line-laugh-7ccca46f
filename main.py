import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    print("wrote {} ({} bytes)".format(dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
