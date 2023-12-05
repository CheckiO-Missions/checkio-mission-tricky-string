from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io_template import CheckiOReferee

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            "python": "tricky_string",
            "js": "trickyString"
        },
        cover_code={
            'python-3': {}
        }
    ).on_ready)