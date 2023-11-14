# Задание 1
def calc_bmi(height_meters: 'int|float', weight_kg: 'int|float'):
    bmi = weight_kg / (height_meters ** 2)
    bmi_categories = {
        (0, 18.5): 'Underweight',
        (18.5, 25): 'Normal weight',
        (25, 30): 'Normal weight',
    }
    for k in bmi_categories:
        left_bound, right_bound = k
        if left_bound < bmi < right_bound:
            return bmi, bmi_categories[k]
    return bmi, 'Obesity'


print(calc_bmi(1.80, 60))


# Задание 2


def name_shape(*args) -> str:
    sides_count = len(args)
    shapes = {
        3: 'Triangle',
        4: 'Square',
        5: 'Pentagon',
        6: 'Hexagon',
        7: 'Heptagon',
        8: 'Octagon',
        9: 'Nonagon',
        10: 'Decagon'
    }
    return shapes.get(sides_count, 'Unknown shape')


# Задание 3

def next_date(year: int, month: int, day: int):
    error_msg = 'Invalid date: {} is out or range ({}-{})'
    if month < 0 or month > 12:
        return error_msg.format('month', 1, 12)
    january = 1
    february = 2
    march = 3
    april = 4
    may = 5
    june = 6
    july = 7
    august = 8
    september = 9
    october = 10
    november = 11
    december = 12
    days_in_months = {
        january: 31,
        february: 28,
        march: 31,
        april: 30,
        may: 31,
        june: 30,
        july: 31,
        august: 31,
        september: 30,
        october: 31,
        november: 30,
        december: 31
    }
    days_in_months_leap = days_in_months.copy()
    days_in_months_leap[february] = 29
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    days_in_current_month = days_in_months_leap[month] if is_leap_year else days_in_months[month]
    if day > days_in_current_month:
        return error_msg.format('day', 1, days_in_current_month)
    month_wraps_around = (day + 1) > days_in_current_month
    next_day = 1 if month_wraps_around else day + 1
    year_wraps_around = month_wraps_around and (month + 1 == 13)
    next_month = month
    if month_wraps_around:
        next_month = 1 if year_wraps_around else month + 1
    next_year = year + 1
    return next_year, next_month, next_day


print(next_date(2000, 12, 31))


# Задание 4


def calc_order_price(items_count: int) -> float:
    if items_count < 1:
        return 0
    first_item_price_cents = 1095
    opt_item_price_cents = 295
    opt_count = items_count - 1
    price_cents = (first_item_price_cents + opt_item_price_cents * opt_count)
    string_repr = str(price_cents)
    integer_part = string_repr[:-2]
    fixed_point_part = string_repr[-2:]
    price_dollars = float(f"{integer_part}.{fixed_point_part}")
    return price_dollars


print(calc_order_price(3))


# Задание 5


def simplify_fraction(numerator: int, denominator: int) -> 'tuple[int,int]':
    def is_prime(number: int) -> bool:
        upper_bound = int(number ** 0.5) + 1
        for i in range(2, upper_bound):
            if not number % i:
                return False
        return True

    def factorize(number: int) -> list:
        factors = list()
        upper_bound = int(number ** 0.5) + 1
        primes_to_consider = [x for x in range(2, upper_bound) if is_prime(x)]
        rem = number
        for prime in primes_to_consider:
            while not rem % prime:
                rem //= prime
                factors.append(prime)
        factors.append(number)
        return factors

    numerator_factors = factorize(numerator)
    denominator_factors = factorize(denominator)
    nf_freq = {
        i: numerator_factors.count(i) for i in numerator_factors
    }
    df_freq = {
        i: denominator_factors.count(i) for i in denominator_factors
    }
    common_factors = {
        k: min(v, df_freq[k]) for k, v in nf_freq.items() if k in df_freq.keys()
    }
    for n in common_factors.keys():
        count = common_factors[n]
        while count > 0:
            numerator //= n
            denominator //= n
            count -= 1
    return numerator, denominator


print(simplify_fraction(60, 123))


# Задание 6


def foo(some_list: 'list[int|str]') -> None:
    def validate_list(arr: list):
        return type(arr) == list and len(arr) > 9 and len(
            [x for x in arr if type(x) not in [int, str]]) == 0

    if not validate_list(some_list):
        return None
    print(some_list[::-1])
    some_list.sort(reverse=True)
    print(some_list)
    some_list.sort(reverse=False)
    print(some_list)
    print(some_list[2:7])
    arr = some_list.copy()
    del arr[4]
    print(arr)
    arr = list(set(some_list))
    print(arr)


foo([x for x in range(10)])


def count_range(iter_item, min_range: 'int|float', max_range: 'int|float') -> int:
    return len([x for x in iter_item if min_range < x <= max_range])


print(count_range([3, 4, 5], 2, 5))


def count_subarrays(arr: list) -> int:
    if type(arr) != list:
        return 0
    total = 1
    for item in arr:
        total += count_subarrays(item)
    return total


print(count_subarrays([1, 2, 2, [1, [], 2, []], []]))


def are_anagram(word_one: str, word_two: str) -> bool:
    return len(set(word_one).difference(set(word_two))) == 0


def to_phone_kb_input(text: str) -> str:
    text = text.strip().upper()
    buttons_to_text = {
        '1': '.,?!',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PRQS',
        '8': 'TUV',
        '9': 'WXYZ',
        '0': ' '
    }
    text_to_buttons = {

    }
    repeat_counts = {

    }
    for k, v in buttons_to_text.items():
        for i, c in enumerate(v):
            repeat_counts[c] = i + 1
            text_to_buttons[c] = k
    input_sequence = str()
    for c in text:
        if c not in text_to_buttons:
            continue
        button = text_to_buttons[c]
        repeat_count = repeat_counts[c]
        input_sequence += button * repeat_count
    return input_sequence


print(to_phone_kb_input('input from phone'))


def flatten(arr: list) -> list:
    result = []
    for item in arr:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


print(flatten([
    1, 2, 3, [4, 5, 6, 6], [3, [324, 24, [2, 3, [3, 4, 53]]]]
]))
