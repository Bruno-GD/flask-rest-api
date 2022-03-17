import pytest
from flaskr import create_app
from flaskr.repository.database import Database


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(autouse=True)
def before_and_after(client):
    # Clear "items" table & insert default items
    Database.init_db()
    with client.application.app_context():
        # Setup database before test
        db = Database.get_db()
        try:
            # Run test
            yield
        finally:
            # Rollback database after test
            db.rollback()
