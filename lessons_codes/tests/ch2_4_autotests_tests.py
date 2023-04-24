#!/usr/bin/env python3

import lessons_codes.ch2_4_autotests as ch2_4


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


def main():
    capitalize_test()
    capitalize_asert()


if __name__ == '__main__':
    main()
