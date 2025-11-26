import unittest
from unittest.mock import patch, MagicMock
from progenomes import view


class TestView(unittest.TestCase):
    def test_get_url(self):
        # Test with a valid item
        url, filetype = view.get_url("highly-important-strains")
        self.assertEqual(
            url, "https://progenomes.embl.de/data/pg4_highly_important_strains.tsv.gz"
        )
        self.assertEqual(filetype, "tsv.gz")

        # Test with another valid item
        url, filetype = view.get_url("excluded-genomes")
        self.assertEqual(
            url, "https://progenomes.embl.de/data/pg4_excluded_genomes.txt.gz"
        )
        self.assertEqual(filetype, "txt.gz")

        # Test with an invalid item
        with self.assertRaises(ValueError):
            view.get_url("invalid-item")


if __name__ == "__main__":
    unittest.main()
