from collections import namedtuple
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

INITIAL_URL = "https://progenomes.embl.de/data"

URLMapping = namedtuple("URLMapping", ["file_prefix", "filename", "filetype"])

URL_MAPPING = {
    "highly-important-strains": URLMapping(
        file_prefix="pg4",
        filename="highly_important_strains",
        filetype="tsv.gz",
    ),
    "excluded-genomes": URLMapping(
        file_prefix="pg4",
        filename="excluded_genomes",
        filetype="txt.gz",
    ),
    "ani-representatives": URLMapping(
        file_prefix="pg4",
        filename="representatives_for_each_ANI_cluster",
        filetype="tsv.gz",
    ),
    "ani-clustering": URLMapping(
        file_prefix="pg4",
        filename="ANI_clustering",
        filetype="tsv.gz",
    ),
    "functional-annotations": URLMapping(
        file_prefix="pg4",
        filename="eggnog_representatives",
        filetype="tsv.gz",
    ),
}


def get_url(item: str):
    try:
        mapping = URL_MAPPING[item]
    except KeyError as exc:
        raise ValueError(f"Item '{item}' not found in URL mapping.") from exc
    path = f"{mapping.file_prefix}_{mapping.filename}.{mapping.filetype}"
    return (f"{INITIAL_URL}/{path}", mapping.filetype)


def view(target):
    import polars as pl

    url, filetype = get_url(target)
    return pl.read_csv(url, separator="\t", has_header=False)
