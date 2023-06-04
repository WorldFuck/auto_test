import pytest

from common.yaml_util import clean_yaml


@pytest.fixture(scope="session",autouse=True)
def clear_data_tokens():
    clean_yaml()