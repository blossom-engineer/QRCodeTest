import os
from os.path import join, dirname, abspath

import qrcode
from PIL import Image

FILE_PATH = abspath(
    join(
        dirname(__file__),
        os.pardir,
        'QR',
        'test_qr.png'
    )
)

# QRコード作成
code = qrcode.make('https://github.com/blossom-engineer/QRCodeTest/tree/main')
code.save(FILE_PATH)