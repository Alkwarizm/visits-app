from typing import Generator, Any

import pytest
from fastapi import FastAPI
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from starlette.testclient import TestClient


@pytest.fixture(scope="session")
def db_engine() -> Generator[Engine, Any, None]:
    """Fixture to provide a database engine for the test database."""

    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        pool_size=2,
        pool_pre_ping=True,
    )

    yield engine

@pytest.fixture
def session(db_engine) -> Generator[Session, None, None]:
    """Transactional fixture for tests."""
    connection = db_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session  # Test runs here

    # Rollback after test
    session.close()
    session.close()
    if transaction.is_active:
        transaction.rollback()
    connection.close()


@pytest.fixture
def app(session) -> FastAPI:
    from main import app

    return app


@pytest.fixture
def client(app: FastAPI) -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client