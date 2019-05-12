import pytest
from python_codes import stack


@pytest.fixture
def pytest_stack():
    return stack.Stack()


def test_create_stack():
    s = stack.Stack()
    assert isinstance(s, stack.Stack)
    assert s.max_slots == stack.DEFAULT_STACK_SIZE
    assert len(s) == 0

    s = stack.Stack(100)
    assert isinstance(s, stack.Stack)
    assert s.max_slots == 100
    assert len(s) == 0

    s = stack.Stack(None)
    assert isinstance(s, stack.Stack)
    assert s.max_slots == stack.DEFAULT_STACK_SIZE
    assert len(s) == 0


def test_push_stack(pytest_stack):
    pytest_stack.push(10)
    pytest_stack.push(11)
    pytest_stack.push(None)
    pytest_stack.push("Hello")
    pytest_stack.push(12.0)
    pytest_stack.push(8+4j)
    pytest_stack.push(True)
    pytest_stack.push(False)
    pytest_stack.push('Some String')
    pytest_stack.push('Final String')

    with pytest.raises(stack.StackOverflow):
        pytest_stack.push(20)


def test_pop_stack(pytest_stack):
    pytest_stack.push("Final String")
    assert pytest_stack.pop() == 'Final String'

    pytest_stack.push(10)
    pytest_stack.push(11)
    pytest_stack.push(None)
    pytest_stack.push("Hello")
    pytest_stack.push(12.0)
    pytest_stack.push(8 + 4j)
    pytest_stack.push(True)
    pytest_stack.push(False)
    pytest_stack.push('Some String')

    assert pytest_stack.pop() == 'Some String'
    assert not pytest_stack.pop()
    assert pytest_stack.pop()
    assert pytest_stack.pop() == 8+4j
    assert pytest_stack.pop() == 12.0
    assert pytest_stack.pop() == "Hello"
    assert not pytest_stack.pop()
    assert pytest_stack.pop() == 11
    assert pytest_stack.pop() == 10

    with pytest.raises(stack.StackUnderflow):
        pytest_stack.pop()


def test_membership_in():
    s = stack.Stack()

    for item in range(6):
        s.push(item)

    for item in range(6):
        assert item in s


def test_membership_not_in():
    s = stack.Stack()

    for item in range(6):
        s.push(item)

    for item in range(6, 20):
        assert item not in s
