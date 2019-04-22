import time
import qrcode

from flask import Flask, request, send_file

app = Flask(__name__)


def create_qrcode(data, with_logo=None):
    """
    Generate QRCode by https://pypi.python.org/pypi/qrcode

    :params string data: The data that contains in QRCode
    :params string with_logo: Logo image path, put logo in QRCode center position
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # TODO: pillow 在 Android 5.1 上有問題，之後 debug
    # if with_logo:
    #     img = img.convert("RGBA")
    #     logo_img = Image.open(with_logo)
    #     box = (135, 135, 235, 235)
    #     img.crop(box)
    #     logo_img = logo_img.resize((box[2] - box[0], box[3] - box[1]))
    #     img.paste(logo_img, box)

    return img


@app.route('/qr', methods=['GET'])
def qr():
    data = request.args.get('data')
    app.logger.info(data)
    image = create_qrcode(data)
    temp_ts = time.time()
    image.save('output/{}.jpg'.format(temp_ts))
    return send_file('output/{}.jpg'.format(temp_ts), mimetype='image/jpeg')
