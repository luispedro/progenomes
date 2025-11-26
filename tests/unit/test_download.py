import unittest
from unittest.mock import patch, call
from progenomes import download


class TestDownload(unittest.TestCase):
    def test_get_genome_url(self):
        # Test case 1: representative-genomes
        url = download._get_genome_url("representative-genomes", "genes")
        expected_url = "https://progenomes.embl.de/data/repGenomes/pg4_genes_representatives.fna.gz"
        self.assertEqual(url, expected_url)

    @patch("urllib.request.urlretrieve")
    def test_download_genomes(self, mock_urlretrieve):
        components = ["genes", "genomes"]
        download.download_genomes("representative-genomes", components)

        # Check that urlretrieve was called with the correct URLs
        expected_calls = [
            call(
                "https://progenomes.embl.de/data/repGenomes/pg4_genes_representatives.fna.gz",
                "pg4_genes_representatives.fna.gz",
            ),
            call(
                "https://progenomes.embl.de/data/repGenomes/pg4_genomes_representatives.fna.gz",
                "pg4_genomes_representatives.fna.gz",
            ),
        ]
        mock_urlretrieve.assert_has_calls(expected_calls, any_order=True)

    def test_get_dataset_url(self):
        # Test case 1: excluded-genomes
        url = download._get_dataset_url("excluded-genomes")
        expected_url = "https://progenomes.embl.de/data/pg4_excluded_genomes.txt.gz"
        self.assertEqual(url, expected_url)

        # Test case 2: highly-important-strains
        url = download._get_dataset_url("highly-important-strains")
        expected_url = (
            "https://progenomes.embl.de/data/pg4_highly_important_strains.tsv.gz"
        )
        self.assertEqual(url, expected_url)

    @patch("urllib.request.urlretrieve")
    def test_download_dataset(self, mock_urlretrieve):
        download.download_dataset("highly-important-strains")
        mock_urlretrieve.assert_called_once_with(
            "https://progenomes.embl.de/data/pg4_highly_important_strains.tsv.gz",
            "pg4_highly_important_strains.tsv.gz",
        )


if __name__ == "__main__":
    unittest.main()
