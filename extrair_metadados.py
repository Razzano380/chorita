"""Lê a data original de fotos e vídeos da pasta midia/ e gera midia.js.

Uso:
    python extrair_metadados.py            # lê ./midia
    python extrair_metadados.py "C:/Fotos"  # copia de outra pasta para ./midia

Fotos: lê o EXIF (DateTimeOriginal). HEIC precisa de `pip install pillow-heif`
e é convertido para JPG, porque Chrome e Firefox não abrem HEIC.
Vídeos: lê creation_time com ffprobe (precisa do ffmpeg instalado).
Legendas e datas que você já escreveu no midia.js são mantidas.
"""
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageOps

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

RAIZ = Path(__file__).resolve().parent
PASTA_MIDIA = RAIZ / "midia"
ARQUIVO_SAIDA = RAIZ / "midia.js"
FOTOS = {".jpg", ".jpeg", ".png", ".heic", ".heif"}
VIDEOS = {".mov", ".mp4", ".m4v"}
TAG_DATA_ORIGINAL, TAG_DATA, IFD_EXIF = 36867, 306, 0x8769


def data_da_foto(caminho):
    with Image.open(caminho) as im:
        exif = im.getexif()
        bruto = exif.get_ifd(IFD_EXIF).get(TAG_DATA_ORIGINAL) or exif.get(TAG_DATA)
    if not bruto:
        return None
    return datetime.strptime(bruto.strip("\x00 "), "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M")


def data_do_video(caminho):
    try:
        saida = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(caminho)],
            capture_output=True, text=True, check=True,
        ).stdout
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    tags = json.loads(saida).get("format", {}).get("tags", {})
    # A data da Apple já vem no fuso local (ex.: 2026-09-19T03:27:09-0300)
    bruto = tags.get("com.apple.quicktime.creationdate") or tags.get("creation_time")
    return bruto[:16] if bruto else None


def converter_para_jpg(caminho):
    destino = caminho.with_suffix(".jpg")
    with Image.open(caminho) as im:
        exif = im.getexif()
        ImageOps.exif_transpose(im).convert("RGB").save(destino, quality=85, exif=exif.tobytes())
    caminho.unlink()
    return destino


def capa_do_video(caminho):
    capa = caminho.with_suffix(".jpg")
    if not capa.exists():
        subprocess.run(
            ["ffmpeg", "-loglevel", "error", "-y", "-ss", "0.3", "-i", str(caminho),
             "-frames:v", "1", "-vf", "scale=640:-2", str(capa)],
            check=False,
        )
    return capa if capa.exists() else None


def carregar_existente():
    if not ARQUIVO_SAIDA.exists():
        return {}
    texto = ARQUIVO_SAIDA.read_text(encoding="utf-8")
    inicio, fim = texto.find("["), texto.rfind("]")
    return {item["arquivo"]: item for item in json.loads(texto[inicio:fim + 1])}


def main():
    PASTA_MIDIA.mkdir(exist_ok=True)
    if len(sys.argv) > 1:
        for arquivo in Path(sys.argv[1]).iterdir():
            if arquivo.suffix.lower() in FOTOS | VIDEOS:
                shutil.copy2(arquivo, PASTA_MIDIA / arquivo.name)

    existente = carregar_existente()
    capas = set()
    itens = []
    for caminho in sorted(PASTA_MIDIA.iterdir()):
        ext = caminho.suffix.lower()
        if ext in VIDEOS:
            data, tipo = data_do_video(caminho), "video"
        elif ext in FOTOS:
            data = data_da_foto(caminho)
            if ext in {".heic", ".heif"}:
                caminho = converter_para_jpg(caminho)
            tipo = "foto"
        else:
            continue
        item = {"arquivo": f"midia/{caminho.name}", "tipo": tipo, "data": data, "legenda": ""}
        if tipo == "video":
            capa = capa_do_video(caminho)
            if capa:
                item["capa"] = f"midia/{capa.name}"
                capas.add(item["capa"])
        anterior = existente.get(item["arquivo"], {})
        item["legenda"] = anterior.get("legenda") or ""
        if not item["data"] and anterior.get("data"):
            item["data"] = anterior["data"]  # data escrita à mão
        itens.append(item)

    itens = [i for i in itens if i["arquivo"] not in capas]
    itens.sort(key=lambda i: (i["data"] is None, i["data"] or "", i["arquivo"]))

    linhas = ",\n".join("  " + json.dumps(i, ensure_ascii=False) for i in itens)
    ARQUIVO_SAIDA.write_text(
        "// Gerado por extrair_metadados.py. \"data\" vem do EXIF/metadado do arquivo.\n"
        "// Pode editar \"legenda\" e \"data\" à mão: o script preserva o que você escreveu.\n"
        f"window.MIDIA = [\n{linhas}\n];\n",
        encoding="utf-8",
    )
    com_data = sum(1 for i in itens if i["data"])
    print(f"{len(itens)} arquivos, {com_data} com data. midia.js atualizado.")


if __name__ == "__main__":
    main()
