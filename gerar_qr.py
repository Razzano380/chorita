"""Gera o QR code que leva ao site publicado.

Uso:
    pip install qrcode pillow
    python gerar_qr.py https://endereco-do-site

Gera qr.png (para mandar no celular ou imprimir) e qr.svg (vetor, para gráfica).
"""
import sys
from pathlib import Path

import qrcode
import qrcode.image.svg

RAIZ = Path(__file__).resolve().parent


def main():
    if len(sys.argv) != 2 or not sys.argv[1].startswith(("http://", "https://")):
        sys.exit("Uso: python gerar_qr.py https://endereco-do-site")
    url = sys.argv[1]

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=24, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="#2b2522", back_color="white").save(RAIZ / "qr.png")

    svg = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage,
                      error_correction=qrcode.constants.ERROR_CORRECT_M)
    svg.save(RAIZ / "qr.svg")
    print(f"qr.png e qr.svg gerados para {url}")


if __name__ == "__main__":
    main()
