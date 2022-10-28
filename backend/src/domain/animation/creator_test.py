import tempfile  # to save it locally
from domain.animation.creator import AnimationCreator
from domain.picsart.client import PicsartImageClient

image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
rmbg = PicsartImageClient(image_url)


result = rmbg.removebg()
print(result)

rmbg_url = result["data"]["url"]
tempFolder = tempfile.mkdtemp()
finalFolder = "resource"

AnimationCreator.downloadByUrl(image_url, 0, tempFolder)
AnimationCreator.downloadByUrl(rmbg_url, 1, tempFolder)

crt = AnimationCreator()
crt.make_gif(f"{finalFolder}/totoro.gif")