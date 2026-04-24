import pytest
import os
from FastQ_files_Biopy import (
    is_within_gc_bounds,
    is_within_length,
    is_quality_satisfied,
    read_file,
    write_result,
    filter_fastq,
)


class TestFilterConditions:
    """Testing logical functions for filtering"""

    def test_gc_bounds(self):
        # test GC calculation
        assert is_within_gc_bounds("ATGC", (40, 60)) is True
        assert is_within_gc_bounds("ATGC", (60, 100)) is False
        assert is_within_gc_bounds("ATGC", (50,)) is True

    def test_length_bounds(self):
        # test sequence length
        assert is_within_length("ATGC", (2, 5)) is True
        assert is_within_length("ATGC", (5, 10)) is False
        assert is_within_length("ATGC", (4,)) is True

    def test_quality_satisfied(self):
        # test quality (Phred)
        assert is_quality_satisfied([30, 30, 30], 30.0) is True
        assert is_quality_satisfied([20, 20], 30.0) is False

    def test_quality_empty_sequence(self):
        # test error handling
        assert is_quality_satisfied([], 30.0) is False


class TestFileOperations:
    """Testing file operations"""

    def test_read_file_error(self):
        with pytest.raises(FileNotFoundError):
            read_file("non_existent_abracadabra.fastq")

    def test_write_and_read_file(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)

        sample_data = {"@seq1": ("ATGC", [30, 30, 30, 30])}
        write_result("test_out.fastq", sample_data)

        expected_path = os.path.join("filtered", "test_out.fastq")
        assert os.path.exists(expected_path)

        read_back = read_file(expected_path)
        assert "@seq1" in read_back
        assert read_back["@seq1"][0] == "ATGC"


class TestIntegration:
    """Integration tests for the entire pipeline"""

    def test_empty_fastq_handling(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with open("empty.fastq", "w") as f:
            pass

        filter_fastq("empty.fastq", output_fastq="empty_out.fastq")
        assert os.path.exists(os.path.join("filtered", "empty_out.fastq"))

    def test_full_pipeline(self, tmp_path, monkeypatch):
        # test of entire pipeline
        monkeypatch.chdir(tmp_path)

        with open("input.fastq", "w") as f:
            f.write("@seq1\nATGC\n+\nIIII\n")
            f.write("@seq2\nATAT\n+\nIIII\n")

        filter_fastq("input.fastq", gc_bounds=(40, 60), output_fastq="out.fastq")

        result = read_file(os.path.join("filtered", "out.fastq"))
        assert "@seq1" in result
        assert "@seq2" not in result
