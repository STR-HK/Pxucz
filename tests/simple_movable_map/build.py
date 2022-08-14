import os

from Pxucz.utils import build

build.build(
    withconsole=True,
    path=os.path.abspath("simple_movable_map.py"),
    filedict=["assets"],
    companyname="Cshtarn",
    product_version="0.0.1",
)
