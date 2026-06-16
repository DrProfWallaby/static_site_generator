import os
import shutil

def main():
        static = os.path.abspath(f"./static")
        public = os.path.abspath(f"./public")
        if os.path.exists(public):
            shutil.rmtree(public)
        static_to_public(static, public)

def static_to_public(src: str, dst: str) -> None:
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        if os.path.isdir(os.path.join(src, item)):
            static_to_public(os.path.join(src, item), os.path.join(dst, item))
        else:
            shutil.copy(os.path.join(src, item), os.path.join(dst, item))



if __name__ == "__main__":
    main()