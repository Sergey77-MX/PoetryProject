import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('input_data, state, expected', [
    (
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
            'EXECUTED',
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    ),
(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
            'CANCELED',
            [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    ),
(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
            '',
            []
    ),
(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
            '123',
            []
    )
])

def test_filter_by_state(input_data, state, expected):
    assert filter_by_state(input_data, state) == expected


@pytest.mark.parametrize('input_data, direction, expected', [
    (
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
            True,
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    ),(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
            False,
            [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             ]
    ),(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-12T21:27:25.241689'}],
            False,
            [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-12T21:27:25.241689'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
             ]
    ),(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14'}],
            False,
            [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             ]
    ),(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
            False,
            [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29'},
             ]
    )
])

def test_sort_by_date(input_data, direction, expected):
    assert sort_by_date(input_data, direction) == expected
