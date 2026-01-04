import pytest
from unittest.mock import MagicMock, patch

from app.service.user_service import UserService


@pytest.fixture
def user_service():
    """
    Equivalent to @BeforeEach in JUnit.
    Creates a UserService with mocked dependencies.
    """
    with patch("app.service.user_service.UserRepository") as MockRepo, \
         patch("app.service.user_service.OrderClient") as MockOrderClient:

        mock_repo = MockRepo.return_value
        mock_order_client = MockOrderClient.return_value

        service = UserService()

        service.repository = mock_repo
        service.order_client = mock_order_client

        yield service


def test_create_user_should_create_user_and_order(user_service):
    user = {"name": "John", "email": "john@email.com"}

    user_service.repository.create.return_value = user

    result = user_service.create_user(user)

    user_service.order_client.create_order.assert_called_once_with(
        price="100",
        quantity="2"
    )
    user_service.repository.create.assert_called_once_with(user)
    assert result == user


def test_list_users(user_service):
    users = [
        {"name": "John"},
        {"name": "Mary"}
    ]

    user_service.repository.find_all.return_value = users

    result = user_service.list_users()

    user_service.repository.find_all.assert_called_once()
    assert result == users


def test_get_user_by_id(user_service):
    user_id = "123"
    user = {"id": user_id, "name": "John"}

    user_service.repository.find_by_id.return_value = user

    result = user_service.get_user(user_id)

    user_service.repository.find_by_id.assert_called_once_with(user_id)
    assert result == user


def test_update_user(user_service):
    user_id = "123"
    data = {"name": "Updated"}

    user_service.update_user(user_id, data)

    user_service.repository.update.assert_called_once_with(user_id, data)


def test_delete_user(user_service):
    user_id = "123"

    user_service.delete_user(user_id)

    user_service.repository.delete.assert_called_once_with(user_id)


def test_create_user_and_order_success(user_service):
    user_service.create_user_and_order("100", "2")

    user_service.order_client.create_order.assert_called_once_with(
        price="100",
        quantity="2"
    )


def test_create_user_and_order_exception_should_not_fail(user_service):
    user_service.order_client.create_order.side_effect = Exception("Order service error")

    # Should NOT raise exception
    user_service.create_user_and_order("100", "2")

    user_service.order_client.create_order.assert_called_once()
