[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI version](https://badge.fury.io/py/progenomes.svg)](https://badge.fury.io/py/progenomes) [![Bioconda version](https://anaconda.org/bioconda/progenomes/badges/version.svg)](https://anaconda.org/bioconda/progenomes)

# proGenomes-cli

proGenomes-cli is a command-line tool for exploring the [proGenomes](https://progenomes.embl.de) dataset of bacterial and archaeal genomes.

If you use this software in a publication please cite:

> Anthony Fullam, Ivica Letunic, Oleksandr M Maistrenko, Alexandre Areias Castro, Luis Pedro Coelho, Anastasiia Grekova, Christian Schudoma, Supriya Khedkar, Mahdi Robbani, Michael Kuhn, Thomas S B Schmidt, Peer Bork, Daniel R Mende, proGenomes4: providing 2 million accurately and consistently annotated high-quality prokaryotic genomes, Nucleic Acids Research, 2025;, gkaf1208, https://doi.org/10.1093/nar/gkaf1208

## Installation

proGenomes-cli can be installed using `pip`:

```bash
pip install progenomes
```

or using `conda` through the bioconda channel:

```bash
conda install -c bioconda progenomes
```

## Usage

After installation, the `progenomes` command provides access to several subcommands:

```bash
progenomes download <options>   # Download genome data
progenomes view <options>       # Inspect downloaded data
```

Refer to the built-in help for full details on available commands.

```bash
progenomes --help
```

## License

This project is licensed under the [MIT License](LICENSE).

