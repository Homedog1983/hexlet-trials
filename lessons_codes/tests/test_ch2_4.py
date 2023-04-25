#!/usr/bin/env python3


import lessons_codes.ch2_4_autotests as ch2_4
from pytest import raises


def capitalize_test():
    if ch2_4.capitalize('hello') != 'Hello':
        raise Exception('Функция работает неверно!')
    if ch2_4.capitalize('') != '':
        raise Exception('Функция работает неверно!')
    print('Все тесты пройдены!')


def capitalize_asert():
    assert ch2_4.capitalize('hello') == 'Hello'
    assert ch2_4.capitalize('') == ''
    assert ch2_4.capitalize('34fgh') == '34fgh'
    assert ch2_4.capitalize('$%^jkl') == '$%^jkl'
    assert ch2_4.capitalize(' ghj') == ' ghj'
    print('Все тесты пройдены!')


################# PYTEST TESTS ################# 
def test_reverse():
    assert ch2_4.reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert ch2_4.reverse('') == ''


# Stack testing
def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_stack_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    with raises(IndexError):
        stack.pop()


def main():
    return True
    # capitalize_test()
    # capitalize_asert()


if __name__ == '__main__':
    main()
