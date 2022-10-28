import base64
from urllib.parse import quote, unquote, urlencode, urlparse

import requests


class PicsartImageClient:
    def __init__(
        self,
        # image_url=f"file://{quote('/workspace/backend/src/domain/animation/resource/totoro/Screen Shot 2022-10-26 at 8.41.38 PM.png')}",
        image_url=f"file://{quote('/workspace/backend/src/domain/animation/resource/totoro/smalll.png')}",
    ):
        self.image_url = image_url
        self.header = {
            "accept": "application/json",
            "apikey": "Q0FAU1mrVgObO2rfStg7Gc2q5b1PgeqO",
        }

        self.url = "https://api.picsart.io/tools/demo/"

    # Remove Background
    def removebg(self):
        body = {
            "output_type": "cutout",  # mask
            "format": "JPG",  # defualt "PNG", support "JPG", "PNG", "TIFF", "WEBP"
            "image_url": self.image_url,
        }

        response = requests.post(
            f"{self.url}removebg",
            headers=self.header,
            data=body,
        )
        # print(response.json())
        if response.status_code == 200:
            return response.json()["data"]["url"]
        return False

    # Change Background Image
    def changeBg(
        self,
        bg_image_url="https://media.wired.com/photos/5eb9dd2b906d2cc75b592871/master/w_960,c_limit/Science_seabreeze_502004639.jpg",
    ):
        body = {
            "output_type": "cutout",  # mask
            "format": "JPG",  # defualt "PNG", support "JPG", "PNG", "TIFF", "WEBP"
            "image_url": self.image_url,
            "bg_image_url": bg_image_url,
        }

        response = requests.post(
            f"{self.url}removebg",
            headers=self.header,
            data=body,
        )
        print(response.json())
        if response.status_code == 200:
            return response.json()["data"]["url"]
        print("Something wrong when changing backgroud image")
        return False

    # Change Background Color
    def changeBgColor(
        self,
        bg_color="#fed71a",
    ):
        body = {
            "output_type": "cutout",  # mask
            "format": "JPG",  # defualt "PNG", support "JPG", "PNG", "TIFF", "WEBP"
            "image_url": self.image_url,
            "bg_color": bg_color,
        }

        response = requests.post(
            f"{self.url}removebg",
            headers=self.header,
            data=body,
        )

        if response.status_code == 200:
            return response.json()["data"]["url"]
        print("Something wrong when changing backgroud image")
        return False

    # Effects
    def getEffectsName(self):

        body = {
            "image_url": self.image_url,
            "format": "JPG",  # default "PNG", support "JPG", "PNG", "TIFF", "WEBP"
        }

        response = requests.get(
            f"{self.url}effects",
            headers=self.header,
            data=body,
        )

        # print(response.json())
        if response.status_code == 200:
            return response.json()["data"]
        return False

    def effectsPreview(self, group):
        effectGroup = {
            1: ["icy1", "icy2", "icy3", "brnz1", "brnz2", "brnz3", "mnch1", "mnch2", "mnch3"],
            2: ["noise", "saturation", "cyber1", "cyber2", "food1", "food2", "nature1", "nature2"],
            3: ["urban1", "urban2", "water1", "water2", "shadow1", "shadow2", "sketcher2"],
        }

        body = {
            "image_url": self.image_url,
            "effect_names": ["icy1", "water1"],
            "preview_size": 240,  # default 120px
            "format": "JPG",  # default "PNG", support "JPG", "PNG", "TIFF", "WEBP"
        }

        response = requests.post(
            f"{self.url}effects/previews",
            headers=self.header,
            data=body,
        )

        print(response.json())
        if response.status_code == 200:
            return response.json()["data"][0]["url"]
        return False

    def effects(self, effectName="icy3"):
        url = self.image_url

        if urlparse(url).scheme == "file":
            url = self.upload()
            if not url:
                return False

        body = {
            "image_url": url,
            # "image_id": '7af58ec4-50fc-4006-85d6-bb322d9a9ee3',
            "effect_name": effectName,
        }
        response = requests.post(
            f"{self.url}effects",
            headers=self.header,
            data=body,
        )

        if response.status_code == 200:
            return response.json()["data"]["url"]
        return False

    def mask(self):
        body = {
            "image_url": self.image_url,
            "format": "JPG",  # default "PNG", support "JPG", "PNG", "TIFF", "WEBP"
            "blend": "",  # normal screen(default) overlay multiply darken lighten add
            "mask": "lace1",  # (required) lace1 lace2 lace3 lace4 shdw2 shdw17 rpl3 rpl5 prsm3 prsm9 prsm10
            "opacity": 100,  # integer from 0 to 100, default is 100.
            "hue": 0,  # integer from -180 to +180. Default is 0.
            "mask_flip": "mirror horizontal",  # left, right, mirror horizontal, mirror vertical, turnaround
        }

        response = requests.post(
            f"{self.url}masks",
            headers=self.header,
            data=body,
        )

        print(response.json())
        """
        {'detail': 'Internal server error'}
        """
        if response.status_code == 200:
            return response.json()["data"]["url"]
        return False

    # Adjust
    def adjust(self):
        pass

    # Style Transfer
    def styleTransfer(self):
        body = {
            "reference_image_url": "https://c-ssl.dtstatic.com/uploads/blog/202104/18/20210418212856_c8890.thumb.300_0.jpeg_webp",
            "format": "JPG",  # default "PNG", support "JPG", "PNG", "TIFF", "WEBP"
            "level": "l3",  # l1, l2, l3, l4, l5
            "image_url": "http://paulgravett.com//articles2/article_images/ZaoDaoSoufle_Boy_Cover_480.jpg",
        }

        response = requests.post(
            f"{self.url}styletransfer",
            headers=self.header,
            data=body,
        )

        print(response.json())
        if response.status_code == 200:
            return response.json()["data"]["url"]
        return False

    # Conversion
    def conversion(self):
        pass

    def upload(self):
        parsed = urlparse(self.image_url)

        # if parsed.scheme != "file":
        #     print("123")
        #     return False

        with open(unquote(parsed.path), "rb") as img_file:
            response = requests.post(
                f"{self.url}upload",
                headers=self.header,
                data={},
                files=[
                    ("image", ("Untitled.png", img_file, "image/png")),
                ],
            )

        print(response.json())
        if response.status_code == 200:
            return response.json()["data"]["url"]
        return False
