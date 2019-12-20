def pytest_addoption(parser):
    parser.addoption('--host', action='store', dest='host', default='http://localhost:5000')
    parser.addoption('--drop-db', action="store_true", dest='drop-db', default=False)
