# Tạo hệ thống mạng lưới nhà khoa học

Module xây dựng hệ thống mạng lưới nhà khoa học.

## Mô tả

Thực hiện trích xuất thông tin và đồ thị hóa.

Tech stack: Neo4j, neomodel, pandas.

## Docs

Tư liệu cho báo cáo: `/professors/docs/`

## Source

Source code: `/professors/src`

## Chạy dự án:

Khởi tạo môi trường:

```bash

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

#set up file .env 
# for neo4j db

pip install -e .



```

Crawl dữ liệu: `python3 src/GraphBuilder/crawl/crawl.py`

Tạo mạng: `python3 src/main.py`

