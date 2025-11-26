from collections import namedtuple
from tqdm import tqdm
import urllib.request
from typing import Union

GENOME_INITIAL_URL = "https://progenomes.embl.de/data"

GenomeUrlData = namedtuple(
    "UrlData", ["type", "server_prefix", "file_prefix", "filetype", "order"]
)

DatasetUrlData = namedtuple(
    "DatasetUrlData", ["file_prefix", "filename", "filetype", "headers"]
)

GENOME_URL_MAPPING = {
    "representative-genomes": GenomeUrlData(
        "representatives", "repGenomes", "pg4", "fna.gz", "target.type"
    ),
}


def _get_genome_url(target: str, component: str):
    mapping = GENOME_URL_MAPPING[target]
    if mapping.order == "type.target":
        return (
            f"{GENOME_INITIAL_URL}/{mapping.server_prefix}/{mapping.file_prefix}."
            f"{mapping.type.replace('-', '_')}.{component}.{mapping.filetype}"
        )
    else:
        return (
            f"{GENOME_INITIAL_URL}/{mapping.server_prefix}/{mapping.file_prefix}_"
            f"{component}_{mapping.type.replace('-', '_')}.{mapping.filetype}"
        )


def download_genomes(target: str, components: list[str]):
    ''' Download genome files by their target name and components. '''
    pbar = tqdm(components)
    for t in pbar:
        pbar.set_description(f"Downloading {t}")
        url = _get_genome_url(target, t)
        print(url)
        urllib.request.urlretrieve(url, url.split("/")[-1])


DATASET_INITIAL_URL = "https://progenomes.embl.de/data"

DATASET_URL_MAPPING = {
    "highly-important-strains": DatasetUrlData(
        "pg4", "highly_important_strains", "tsv.gz", False
    ),
    "excluded-genomes": DatasetUrlData(
        "proGenomes3", "excluded_genomes", "txt.bz2", None
    ),
    "mge-orfs": DatasetUrlData("representatives", "mge_ORFS", "tsv.bz2", True),
    "mge-annotation": DatasetUrlData(
        "representatives", "mge_annotation", "tsv.bz2", True
    ),
    "gecco-gene-clusters": DatasetUrlData(
        "proGenomes3", "gecco_clusters", "gbk.gz", None
    ),
}


def _get_dataset_url(item: str):
    mapping = DATASET_URL_MAPPING[item]
    if mapping.file_prefix is None:
        return f"{DATASET_INITIAL_URL}/{mapping.filename}.{mapping.filetype}"
    else:
        return (
            f"{DATASET_INITIAL_URL}/{mapping.file_prefix}_{mapping.filename}."
            f"{mapping.filetype}"
        )


def download_dataset(target: str):
    ''' Download a dataset by its target name. '''
    url = _get_dataset_url(target)
    urllib.request.urlretrieve(url, url.split("/")[-1])
