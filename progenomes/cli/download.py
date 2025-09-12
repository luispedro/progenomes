from tqdm import tqdm
import time
import urllib.request
from typing import Union

GENOME_INITIAL_URL = "https://progenomes.embl.de/data"

GENOME_URL_MAPPING = [
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


def process_genome_url(target: str, component: str):
    mapping = next(iter(item for item in GENOME_URL_MAPPING if item["name"] == target))
    if mapping["order"] == "type.target":
        return f"{GENOME_INITIAL_URL}/{mapping['server-prefix']}/{mapping['file-prefix']}.{mapping['type'].replace('-', '_')}.{component}.{mapping['filetype']}"
    else:
        return f"{GENOME_INITIAL_URL}/{mapping['server-prefix']}/{mapping['file-prefix']}.{component}.{mapping['type'].replace('-', '_')}.{mapping['filetype']}"

def download_genomes(target:str, components: list):
    if len(components)>1:
        pbar = tqdm(components)
        for t in pbar:
            pbar.set_description(f"Downloading {t}")
            url = process_genome_url(target, t)
            print(url)
            # urllib.request.urlretrieve(url, url.split("/")[-1])
            time.sleep(1.0)
    else:
        url = process_genome_url(target, components[0])
        print(url)
        # urllib.request.urlretrieve(url, url.split("/")[-1])
        time.sleep(1.0)


DATASET_INITIAL_URL = "https://progenomes.embl.de/data"

DATASET_URL_MAPPING = [
    {
        "name": "habitats-per-isolate",
        "file-prefix": "proGenomes3",
        "filename": "habitat_isolates",
        "filetype": "tab.bz2",
        "headers": True,
    },
    {
        "name": "habitats-per-speci-cluster",
        "file-prefix": "proGenomes3",
        "filename": "habitat_specI",
        "filetype": "tab.bz2",
        "headers": True,
    },
    {
        "name": "representatives-per-speci-cluster",
        "file-prefix": "proGenomes3",
        "filename": "representatives_for_each_specI",
        "filetype": "tsv.gz",
        "headers": False,
    },
    {
        "name": "marker-genes",
        "file-prefix": "proGenomes3",
        "filename": "markerGenes",
        "filetype": "tar.gz",
    },
    {
        "name": "speci-clustering-data",
        "file-prefix": "proGenomes3",
        "filename": "specI_clustering",
        "filetype": "tab.bz2",
        "headers": False,
    },
    {
        "name": "gtdb-taxonomy",
        "file-prefix": "proGenomes3",
        "filename": "specI_lineageGTDB",
        "filetype": "tab.bz2",
        "headers": True,
    },
    {
        "name": "highly-important-strains",
        "file-prefix": None,
        "filename": "highly_important_strains",
        "filetype": "tab.bz2",
        "headers": False,
    },
    {
        "name": "excluded-genomes",
        "file-prefix": "proGenomes3",
        "filename": "excluded_genomes",
        "filetype": "txt.bz2",
    },
    {
        "name": "mge-orfs",
        "file-prefix": "representatives",
        "filename": "mge_ORFS",
        "filetype": "tsv.bz2",
        "headers": True,
    },
    {
        "name": "mge-annotation",
        "file-prefix": "representatives",
        "filename": "mge_annotation",
        "filetype": "tsv.bz2",
        "headers": True,
    },
    {
        "name": "gecco-gene-clusters",
        "file-prefix": "proGenomes3",
        "filename": "gecco_clusters",
        "filetype": "gbk.gz",
    },
]


def process_dataset_url(item: str):
    mapping = next(iter(i for i in DATASET_URL_MAPPING if i["name"] == item))
    if mapping["file-prefix"] is None:
        return f"{DATASET_INITIAL_URL}/{mapping['filename']}.{mapping['filetype']}"
    else:
        return f"{DATASET_INITIAL_URL}/{mapping['file-prefix']}_{mapping['filename']}.{mapping['filetype']}"

def download_dataset(target:str):
    url = process_dataset_url(target)
    print(url)
    # urllib.request.urlretrieve(url, url.split("/")[-1])
    time.sleep(1.0)

def download(type: str, target: str, components: Union[list, None]):
    print(locals())
    if type == "genomes":
        download_genomes(target, components)
    else: 
        download_dataset(target)
