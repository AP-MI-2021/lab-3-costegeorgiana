import math
from typing import List


def show_menu():
    print('1.Citire date.')
    print('2.Determinare cea mai lunga secventa cu proprietatea ca toate numerele sunt pare.')
    print('3.Determinare cea mai lunga secventa cu proprietatea ca toate numerele sunt formate din cifre prime.')
    print('4.Determinare cea mai lunga secventa cu proprietatea ca toate numerele sunt patrate perfecte.')
    print('5.Iesire')


def read_list() -> List[int]:
    lst = []
    lst_str = input('Scrieti numerele separandu-le printr-un spatiu.')
    lst_str_split = lst_str.split(' ')
    for numar in lst_str_split:
        lst.append(int(numar))
    return lst


def get_longest_all_even(lst: List[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa in care toate elementele sunt pare.
    Input:
    -lst : Lista in care se cauta subsecventa
    Output:
    -subsecventa gasita
    """
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_even = True
            for num in lst[st:dr + 1]:
                if num % 2 != 0:
                    all_even = False
                    break
            if all_even:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def get_is_prime(n):
    """
    Determina daca un numar este prim.
    :param n: numarul care va fi verificat
    :return: true daca numarul este prim, false daca numarul nu este prim
    """
    nr = 0
    for div in range(2, n // 2):
        if n % div == 0:
            nr = nr + 1
    if nr == 0:
        return True
    else:
        return False


def get_all_prime_digits(m):
    """
    Determina daca un numar este format numai din cifre prime.
    :param m: numarul care va fi verificat
    :return: true daca numarul este format doar din cifre prime, false altfel
    """
    ok = 0
    numar = m
    while ok == 0 and numar != 0:
        if not get_is_prime(int(numar % 10)):
            ok = 1
        numar = numar // 10
    if ok == 0:
        return True
    else:
        return False


def get_longest_prime_digits(lst: List[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa care contine numerele formate din cifre prime.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita.
    """
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_prime_digits = True
            for num in lst[st:dr + 1]:
                if not get_all_prime_digits(num):
                    all_prime_digits = False
                    break
            if all_prime_digits:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def get_is_perfect_squares(n):
    """
    Determina daca un numar este patrat perfect.
    :param n: numarul care va fi verificat
    :return: true daca numarul este patrat perfect, false altfel
    """
    if int(math.sqrt(n)) == math.sqrt(n):
        return True
    else:
        return False


def get_longest_all_perfect_squares(lst: List[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa care contine toate numerele patrate perfecte.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    """
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_perfect_squares = True
            for num in lst[st:dr + 1]:
                if not get_is_perfect_squares(num):
                    all_perfect_squares = False
                    break
            if all_perfect_squares:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def test_get_longest_all_even():
    assert get_longest_all_even([1, 2, 4, 6, 5, 6, 4, 7, 9]) == [2, 4, 6]
    assert get_longest_all_even([1, 3, 5, 8, 10, 11, 13]) == [8, 10]
    assert get_longest_all_even([1, 2, 3, 5, 7, 9]) == [2]
    assert get_longest_all_even([3, 5, 7]) == []


def test_get_is_prime():
    assert get_is_prime(3) == True
    assert get_is_prime(6) == False
    assert get_is_prime(7) == True
    assert get_is_prime(11) == True
    assert get_is_prime(12) == False


def test_get_all_prime_digits():
    assert get_all_prime_digits(135) == True
    assert get_all_prime_digits(16) == False
    assert get_all_prime_digits(371) == True
    assert get_all_prime_digits(83) == False
    assert get_all_prime_digits(36) == False


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([83, 33, 65, 56, 800, 631]) == [33]
    assert get_longest_prime_digits([33, 15, 57, 73, 88, 17]) == [33, 15, 57, 73]
    assert get_longest_prime_digits([39, 293, 689, 66]) == []
    assert get_longest_prime_digits([17, 66, 37, 71, 83, 80]) == [37, 71]


def test_get_is_perfect_squares():
    assert get_is_perfect_squares(6) == False
    assert get_is_perfect_squares(4) == True
    assert get_is_perfect_squares(49) == True
    assert get_is_perfect_squares(13) == False
    assert get_is_perfect_squares(25) == True


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([11, 36, 25, 14]) == [36, 25]
    assert get_longest_all_perfect_squares([32, 144, 23, 67]) == [144]
    assert get_longest_all_perfect_squares([9, 5, 25, 64, 97]) == [25, 64]
    assert get_longest_all_perfect_squares([13, 15, 28]) == []


def main():
    lst = []
    while True:
        show_menu()
        optiune = input('Optiunea: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print('Cea mai lunga subsecventa cu toate numerele pare este:', get_longest_all_even(lst))
        elif optiune == '3':
            print('Cea mai lunga subsecventa cu toate numerele formate din cifre prime este:',
                  get_longest_prime_digits(lst))
        elif optiune == '4':
            print('Cea mai lunga subsecventa formata din numere patrate perfecte este:',
                  get_longest_all_perfect_squares(lst))
        elif optiune == '5':
            break


if __name__ == '__main__':
    test_get_longest_all_even()
    test_get_is_prime()
    test_get_all_prime_digits()
    test_get_longest_prime_digits()
    test_get_is_perfect_squares()
    test_get_longest_all_perfect_squares()
    main()
