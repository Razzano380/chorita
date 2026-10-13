# Contrato

Site estático. Para editar:

- `dados.js`: textos do contrato e datas marcantes.
- `midia.js`: fotos e vídeos (data e legenda).
- `python extrair_metadados.py "pasta/com/originais"`: copia as fotos para `midia/` e lê a data do EXIF.
- `python gerar_qr.py https://...`: gera `qr.png` e `qr.svg`.
