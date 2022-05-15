from task_1 import Fraction
from task_2 import Point2D
from task_3 import Point3D

if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(5, 8)

    print(f'''
    {'-'*20}Fraction{'-'*20}
        f1 = {f1}
        f2 = {f2}
        f1 + f2 = {(f1 + f2).__str__():^10} = {Fraction.add(f1,f2)}
        f1 - f2 = {(f1 - f2).__str__():^10} = {Fraction.sub(f1,f2)}
        f1 * f2 = {(f1 * f2).__str__():^10} = {Fraction.mull(f1,f2)}
        f1 / f2 = {(f1 / f2).__str__():^10} = {Fraction.div(f1,f2)}
    ''')

    str_fraction = '1/2'
    fraction_from_string = Fraction.init_from_string(str_fraction)
    print(f'''
        '{str_fraction}' = {fraction_from_string}
    ''')

    p1 = Point2D(1, 2)
    p2 = Point2D(1, 0)
    print(f'''
    {'-'*20}Point2D{'-'*20}
        distance = {p1.distance(p2)}
        amount of instances = {Point2D.amount_of_instances}
    ''')

    p1 = Point3D(1, 4, 1)
    p2 = Point3D(1, 0, 1)
    print(f'''
    {'-'*20}Point3D{'-'*20}
        distance = {p1.distance(p2)}
    ''')
