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
]


def get_url(item: str):
    for mapping in URL_MAPPING:
        if mapping["name"] == item:
            break
    else:
        raise ValueError(f"Item '{item}' not found in URL mapping.")
    mapping = next(iter(i for i in URL_MAPPING if i["name"] == item), None)
    if mapping["file-prefix"] is None:
        path = f"{mapping['filename']}.{mapping['filetype']}"
    else:
        path = f"{mapping['file-prefix']}_{mapping['filename']}.{mapping['filetype']}"
    return (
        f"{INITIAL_URL}/{path}", mapping["filetype"],
    )


def view(target):
    import polars as pl
    import pandas as pd
    url, filetype = get_url(target)
    if "tab.bz2" in filetype:
        return pl.from_pandas(pd.read_table(url))
    elif "tsv.bz2" in filetype:
        return pl.from_pandas(pd.read_csv(url, sep="\t", index_col=None), include_index=False)
    else:
        return pl.read_csv(url, separator="\t")
