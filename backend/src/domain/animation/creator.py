import glob
import os

import requests
from PIL import Image


class AnimationCreator:
    def __init__(
        self,
        frame_folder=os.path.join(
            os.path.dirname(__file__),
            "resource/totoro",
        ),
    ):
        self.frame_folder = frame_folder

    def make_gif(
        self,
        filepath=os.path.join(
            os.path.dirname(__file__),
            "resource",
        ),
        filename="totoro_bg",
        shrink=1,
    ):
        output = os.path.join(filepath, f"{filename}.gif")
        files = sorted(glob.glob(f"{self.frame_folder}/**/*", recursive=True))
        frames = [Image.open(image) for image in files]
        for i in range(len(frames)):
            size = frames[i].size
            frames[i] = frames[i].resize(
                (size[0] // shrink, size[1] // shrink),
            )

        frame_one = frames[0]
        frame_one.save(
            output,
            format="GIF",
            append_images=frames,
            save_all=True,
            duration=200,
            loop=0,
        )

    def downloadByUrl(self, image_url, foldername, index):
        if not os.path.exists(foldername):
            os.makedirs(foldername)  # create folder if it does not exist

        filename = f"{chr(ord('a') + index)}.jpg"
        file_path = os.path.join(foldername, filename)

        r = requests.get(image_url, stream=True)

        if r.status_code == 200:

            with open(file_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
            # # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            # r.raw.decode_content = True
            # # Open a local file with wb ( write binary ) permission.
            # with open(f"{foldername}/{filename}", "wb") as f:
            #     shutil.copyfileobj(r.raw, f)

            print("Image sucessfully Downloaded in", file_path)
        else:
            print("Image Couldn't be retreived")
