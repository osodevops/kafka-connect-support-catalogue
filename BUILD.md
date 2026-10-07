# Build the service overview

The public PDF contains generic OSO service information. Its editable source is `docs/service-overview.json`; the README contains the web-readable catalogue, backed by `docs/connector-catalogue.json`.

## Regenerate

Use Python 3.11 or later:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_pdf.py
```

The builder writes `output/pdf/OSO_Kafka_Connect_Support_and_Services.pdf` and rejects overflowing page content. Render every page and visually review it before publishing, for example with Poppler:

```sh
mkdir -p tmp/pdf-review
pdftoppm -scale-to 1400 -png output/pdf/OSO_Kafka_Connect_Support_and_Services.pdf tmp/pdf-review/page
```

Update the README and overview together when service scope changes. Keep connector release commitments linked to each product's current published policy. Approve the exact connector/runtime combination before calling it tested.

## Assets

`assets/oso-logo.png` and `assets/cover-background.png` are OSO brand assets. Lexend and Space Grotesk font files are bundled with their SIL Open Font License notices in `assets/fonts/`.
