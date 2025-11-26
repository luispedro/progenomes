from progenomes.download import download_dataset, download_genomes
from progenomes.view import view
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="""
    Interact with the proGenomes[1] database.

    [1] - Anthony Fullam, Ivica Letunic, Oleksandr M Maistrenko, Alexandre Areias
    Castro, Luis Pedro Coelho, Anastasiia Grekova, Christian Schudoma, Supriya
    Khedkar, Mahdi Robbani, Michael Kuhn, Thomas S B Schmidt, Peer Bork, Daniel
    R Mende, proGenomes4: providing 2 million accurately and consistently
    annotated high-quality prokaryotic genomes, Nucleic Acids Research, 2025;,
    gkaf1208, https://doi.org/10.1093/nar/gkaf1208
    """,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(help="subcommand help", dest="action")
    parser_download = subparsers.add_parser(
        "download", help="download data from an item"
    )
    subparser_download = parser_download.add_subparsers(
        help="subsubcommand help", dest="download_target"
    )
    parser_download_genome = subparser_download.add_parser(
        "genomes", help="download genome set"
    )
    parser_download_genome.add_argument(
        dest="target",
        choices=[
            "representative-genomes",
        ],
        action="store",
        help="""Representative genome set to download. Available options:
        Representative genomes.""",
    )
    parser_download_genome.add_argument(
        "-c", "--contigs", dest="contigs", help="Contigs", action="store_true"
    )
    parser_download_genome.add_argument(
        "-g", "--genes", dest="genes", help="Genes", action="store_true"
    )
    parser_download_genome.add_argument(
        "-p", "--proteins", dest="proteins", help="Proteins", action="store_true"
    )
    parser_download_genome.add_argument(
        "-a", "--all", dest="all", help="All", action="store_true"
    )
    parser_download_dataset = subparser_download.add_parser(
        "datasets", help="download genome set"
    )
    parser_download_dataset.add_argument(
        dest="target",
        choices=[
            "highly-important-strains",
            "excluded-genomes",
            "ani-representatives",
            "ani-clustering",
            "functional-annotations",
        ],
        action="store",
        help="""Dataset to download. Available options:
        Highly important strains, Excluded genomes, ANI representatives, ANI clustering,
        Functional annotations for representative genomes.""",
    )
    parser_view = subparsers.add_parser("view", help="view an item")
    parser_view.add_argument(
        dest="target",
        choices=[
            "highly-important-strains",
            "excluded-genomes",
            "ani-representatives",
            "ani-clustering",
            "functional-annotations",
        ],
        action="store",
        help="""Dataset to view. Available options:
        Highly important strains, Excluded genomes, ANI representatives, ANI clustering,
        Functional annotations for representative genomes.""",
    )

    args = parser.parse_args()
    if args.action == "download":
        items_to_download = []
        if args.download_target == "genomes":
            if not args.contigs and not args.genes and not args.proteins:
                args.all = True
            if args.contigs:
                items_to_download.append("genomes")
            if args.genes:
                items_to_download.append("genes")
            if args.proteins:
                items_to_download.append("proteins")
            if args.all:
                items_to_download = ["genes", "genomes", "proteins"]
            download_genomes(args.target, items_to_download)
        else:
            items_to_download = None
            download_dataset(args.target)
    elif args.action == "view":
        item_to_view = args.target
        print(view(item_to_view))


if __name__ == "__main__":
    main()
