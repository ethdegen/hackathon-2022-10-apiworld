import os

from domain.picsart.client import PicsartImageClient

client = PicsartImageClient(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../animation/resource/totoro_green.gif",
        )
    )
)
test = client.upload()
print(test)
