from tqdm import tqdm
import time
import urllib.request

INITIAL_URL = "https://progenomes.embl.de/data"

URL_MAPPING = [
    {
        "name": "representative-genomes",
        "type": "representatives",
        "server-prefix": "repGenomes",
        "file-prefix": "progenomes3",
        "filetype": "fasta.bz2",
        "order": "target.type",
    },
    {
        "name": "aquatic",
        "type": "aquatic",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
    {
        "name": "disease-associated",
        "type": "disease-associated",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
    {
        "name": "food-associated",
        "type": "food-associated",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
    {
        "name": "freshwater",
        "type": "freshwater",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
    {
        "name": "host-associated",
        "type": "host-associated",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
    {
        "name": "host-plant-associated",
        "type": "host-plant-associated",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
    {
        "name": "sediment-mud",
        "type": "sediment-mud",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
    {
        "name": "mud",
        "type": "mud",
        "server-prefix": "habitats",
        "file-prefix": "representatives",
        "filetype": "fasta.gz",
        "order": "type.target",
    },
]


def process_url(type: str, target: str):
    mapping = next(iter(item for item in URL_MAPPING if item["name"] == type), None)
    if mapping["order"] == "type.target":
        return f"{INITIAL_URL}/{mapping['server-prefix']}/{mapping['file-prefix']}.{mapping['type'].replace('-', '_')}.{target}.{mapping['filetype']}"
    else:
        return f"{INITIAL_URL}/{mapping['server-prefix']}/{mapping['file-prefix']}.{target}.{mapping['type'].replace('-', '_')}.{mapping['filetype']}"


def download(type: str, targets: list):
    pbar = tqdm(targets)
    for t in pbar:
        pbar.set_description(f"Downloading {t}")
        url = process_url(type, t)
        print(url)
        # urllib.request.urlretrieve(url, url.split("/")[-1])
        time.sleep(1.0)
