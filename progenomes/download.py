from collections import namedtuple
from tqdm import tqdm
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context


GENOME_INITIAL_URL = "https://progenomes.embl.de/data"

GenomeUrlData = namedtuple(
    "UrlData", ["type", "server_prefix", "file_prefix", "filetype"]
)

DatasetUrlData = namedtuple("DatasetUrlData", ["file_prefix", "filename", "filetype"])

GENOME_URL_MAPPING = {
    "representative-genomes": GenomeUrlData(
        "representatives", "repGenomes", "pg4", "fna.gz"
    ),
}


def _get_genome_url(target: str, component: str):
    mapping = GENOME_URL_MAPPING[target]
    return (
        f"{GENOME_INITIAL_URL}/{mapping.server_prefix}/{mapping.file_prefix}_"
        f"{component}_{mapping.type.replace('-', '_')}.{mapping.filetype}"
    )


def download_genomes(target: str, components: list[str]):
    """Download genome files by their target name and components."""
    pbar = tqdm(components)
    for t in pbar:
        pbar.set_description(f"Downloading {t}")
        url = _get_genome_url(target, t)
        print(url)
        urllib.request.urlretrieve(url, url.split("/")[-1])


DATASET_INITIAL_URL = "https://progenomes.embl.de/data"

DATASET_URL_MAPPING = {
    "highly-important-strains": DatasetUrlData(
        "pg4", "highly_important_strains", "tsv.gz"
    ),
    "excluded-genomes": DatasetUrlData("pg4", "excluded_genomes", "txt.gz"),
    "ani-representatives": DatasetUrlData(
        "pg4", "representatives_for_each_ANI_cluster", "tsv.gz"
    ),
    "ani-clustering": DatasetUrlData("pg4", "ANI_clustering", "tsv.gz"),
    "functional-annotations": DatasetUrlData("pg4", "eggnog_representatives", "tsv.gz"),
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
    """Download a dataset by its target name."""
    url = _get_dataset_url(target)
    urllib.request.urlretrieve(url, url.split("/")[-1])
