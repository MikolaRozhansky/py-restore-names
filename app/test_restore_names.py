import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_input, result",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            id="Test 1"
        ),

    ]
)
def test_modify(
        list_input: list,
        result: list,
) -> None:
    restore_names(list_input)
    assert list_input == result
