from unittest.mock import Mock
import pytest
from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/74071424?v=4'
    resp_mock.json.return_value = {
        'login': 'peustratt', 'id': 74071424, 'node_id': 'MDQ6VXNlcjc0MDcxNDI0',
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('peustratt')
    assert 'https://avatars.githubusercontent.com/u/74071424?v=4' == url


def test_buscar_avatar_integração():
    url = github_api.buscar_avatar('yanofelix')
    assert 'https://avatars.githubusercontent.com/u/62208883?v=4' == url
