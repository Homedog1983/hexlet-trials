#!/usr/bin/env python3

import lessons_codes.ch2_4_autotests as ch2_4


def capitalize_test():
    if ch2_4.capitalize('hello') != 'Hello':
        raise Exception('Функция работает неверно!')
    if ch2_4.capitalize('') != '':
        raise Exception('Функция работает неверно!')
    print('Все тесты пройдены!')


def main():
    capitalize_test()


if __name__ == '__main__':
    main()
