def is_within_gc_bounds(seq: str, gc_bounds: tuple[float]) -> bool:
    """
    Filter a sequence by GC content.

    Calculates the GC percentage and checks if it falls within the
    provided bounds. If one bound is given, it is treated as an upper limit.
    """
    count_gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    if len(gc_bounds) == 1:
        up_bound = gc_bounds[0]
        return count_gc <= up_bound
    elif len(gc_bounds) == 2:
        low_bound = gc_bounds[0]
        up_bound = gc_bounds[1]
        return low_bound <= count_gc <= up_bound


def is_within_length(seq: str, length_bounds: tuple[int]) -> bool:
    """
    Filter a sequence by its length.

    Checks if the sequence length is within the specified bounds.
    A single value means an upper limit.
    """
    length_seq = len(seq)
    if len(length_bounds) == 1:
        up_bound = length_bounds[0]
        return length_seq <= up_bound
    elif len(length_bounds) == 2:
        low_bound = length_bounds[0]
        up_bound = length_bounds[1]
        return low_bound <= length_seq <= up_bound


def is_quality_satisfied(quality_seq: str, quality_threshold: int) -> bool:
    """
    Filter a sequence by average Phred quality score.

    Converts ASCII-encoded quality symbols to scores and checks
    if the mean value meets or exceeds the threshold.
    """
    score_sum = 0
    for symbol in quality_seq:
        a = ord(symbol) - 33
        score_sum += a
    mean_score = score_sum / len(quality_seq)
    return mean_score >= quality_threshold
