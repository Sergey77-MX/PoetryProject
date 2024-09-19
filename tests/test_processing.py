import pytest

from src.processing import filter_by_state, sort_by_date


#@pytest.mark.parametrize('list_of_dict, final_list_of_dict', ([{'id': 41428829, 'state': 'EXECUTED'}, {'id': 939719570, 'state': 'EXECUTED'}, {'id': 594226727, 'state': 'CANCELED'}, {'id': 615064591, 'state': 'CANCELED'}]), ([{'id': 594226727, 'state': 'CANCELED'}, {'id': 615064591, 'state': 'CANCELED'}]))


#def test_filter_by_state(list_of_dict, final_list_of_dict):
 #   return filter_by_state(list_of_dict) == final_list_of_dict


