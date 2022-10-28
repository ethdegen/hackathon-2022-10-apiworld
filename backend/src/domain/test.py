import os
import shutil
import tempfile  # to save it locally

from PIL import Image

from domain import animation
from domain.animation.creator import AnimationCreator
from domain.notion.client import NotionClient
from domain.picsart.client import PicsartImageClient

notion = NotionClient(
    "secret_ThyBFJOGvfg9verCNa3So5dK3e8eGeZ5030j05XsWjn",
    "1bd18ec17cf84683bc2eb71c4fb233d7",
    "0ed9a0d3c83f4b6abf23c87cfa26ed0c",
)
# get image url from Notion Page
page_id = "de32e778309648648c27fef0e74e3d4a"
urls_notion = notion.getURL(page_id)

# upload image to Picsart and add effects
tempFolder = tempfile.mkdtemp()
finalFolder = "/workspace/backend/src/domain/animation/resource"
animation = AnimationCreator(tempFolder)

for i, url in enumerate(urls_notion):
    bg_object = PicsartImageClient(url)
    bgChanged = bg_object.changeBgColor("#1a6840")
    object = PicsartImageClient(bgChanged)
    image_url = object.effects("icy1")
    # bgChanged = object.removebg()
    animation.downloadByUrl(image_url, tempFolder, i)

animation.make_gif(
    filepath=os.path.join(
        os.path.dirname(__file__),
        "animation/resource",
    ),
    filename="totoro_green",
    shrink=5,
)


gif = PicsartImageClient(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "animation/resource/totoro_green.gif",
        )
    )
)

url_gif = gif.upload()

notion.embed_add(page_id, url_gif)

shutil.rmtree(tempFolder)
