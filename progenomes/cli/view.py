import polars as pl
import pandas as pd

INITIAL_URL = "https://progenomes.embl.de/data"

URL_MAPPING = [
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
    # {
    #     "name": "marker-genes",
    #     "file-prefix": "proGenomes3",
    #     "filename": "markerGenes",
    #     "filetype": "tar.gz",
    # },
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
    # {
    #     "name": "excluded-genomes",
    #     "file-prefix": "proGenomes3",
    #     "filename": "excluded_genomes",
    #     "filetype": "txt.bz2",
    # },
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
    # {
    #     "name": "gecco-gene-clusters",
    #     "file-prefix": "proGenomes3",
    #     "filename": "gecco_clusters",
    #     "filetype": "gbk.gz",
    # },
]


def process_url(item: str):
    mapping = next(iter(i for i in URL_MAPPING if i["name"] == item))
    if mapping["file-prefix"] is None:
        return f"{INITIAL_URL}/{mapping['filename']}.{mapping['filetype']}", mapping[
            "filetype"
        ]
    else:
        return (
            f"{INITIAL_URL}/{mapping['file-prefix']}_{mapping['filename']}.{mapping['filetype']}",
            mapping["filetype"],
        )


def view(target):
    print(locals())
    # url, filetype = process_url(target)
    # if "tab.bz2" in filetype:
    #     return pl.from_pandas(pd.read_table(url))
    # elif "tsv.bz2" in filetype:
    #     return pl.from_pandas(pd.read_csv(url, sep="\t", index_col=None), include_index=False)
    # else:
    #     return pl.read_csv(url, separator="\t")
