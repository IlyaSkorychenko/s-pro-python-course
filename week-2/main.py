# task-1
class FormulaError(Exception):
    def __init__(self, message='Formula should have format: "float_number [+,-,*,/] float_number}"') -> None:
        super().__init__(message)


def calculator(parse_str: str):
    operators = frozenset({'+', '-', '*', '/'})
    try:
        [first_number, operator, second_number] = parse_str.strip().split()
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        raise FormulaError
    else:
        if operator not in operators:
            raise FormulaError

        match operator:
            case '+':
                return first_number + second_number
            case '-':
                return first_number - second_number
            case '*':
                return first_number * second_number
            case '/':
                return first_number / second_number


# task-2
class ReverseIter:
    def __init__(self, iter_list: []) -> None:
        self.iter_list = iter_list

    def __iter__(self):
        self.index = len(self.iter_list) - 1

        return self

    def __next__(self):
        temp_index = self.index
        self.index -= 1

        if temp_index < 0:
            raise StopIteration

        return self.iter_list[temp_index]


# task-3
def fib_generator(numbers_amount: int):
    current_number = 0
    prev_number = 0

    for i in range(numbers_amount):
        yield current_number
        if current_number == 0:
            current_number += 1
        else:
            temp = current_number
            current_number += prev_number
            prev_number = temp


def fib_list(numbers_amount: int):
    numbers_list = []
    number = 0

    for i in range(numbers_amount):
        numbers_list.append(number)

        if len(numbers_list) == 1:
            number += 1
        else:
            number = numbers_list[i-1] + number

    return numbers_list


if __name__ == '__main__':
    separator = '-' * 10
    print(f'{separator}task-1{separator}')
    print(calculator('2 * 2'))

    print(f'{separator}task-2{separator}')
    reverse_iterator = ReverseIter([x for x in range(10)])
    for element in reverse_iterator:
        print(element)

    print(f'{separator}task-3{separator}')
    print(list(fib_generator(11)))
    print(fib_list(11))
