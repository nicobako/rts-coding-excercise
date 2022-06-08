
import pytest
import code_exercise as ce

@pytest.mark.parametrize(
    ["sequence", "value", "expected"],
    [
        ([1, 5, 2, 1, 10], 6, dict(above=1, below=4)),
        ([1,5,2,10], 5, dict(above=1, below=2)),
    ]
)
def test_above_below(
    sequence,
    value,
    expected,
):
    sc = ce.SequenceComparison()
    actual = sc.above_below(sequence, value)
    assert expected == actual


