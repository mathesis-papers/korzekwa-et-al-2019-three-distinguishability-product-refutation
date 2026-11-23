import itertools
import json
from fractions import Fraction


class Cyclotomic:
    def __init__(self, coefficients=()):
        values = [Fraction(value) for value in coefficients]
        values += [Fraction(0)] * max(0, 4 - len(values))
        for degree in range(len(values) - 1, 3, -1):
            leading = values[degree]
            for shift, coefficient in enumerate([-1, 1, -1, 1]):
                values[degree - 4 + shift] += leading * coefficient
        self.coefficients = tuple(values[:4])

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Cyclotomic) else Cyclotomic([value])

    def __add__(self, other):
        other = self.coerce(other)
        return Cyclotomic([left + right for left, right in zip(self.coefficients, other.coefficients)])

    __radd__ = __add__

    def __neg__(self):
        return Cyclotomic([-value for value in self.coefficients])

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        coefficients = [Fraction(0)] * 7
        for left_index, left in enumerate(self.coefficients):
            for right_index, right in enumerate(other.coefficients):
                coefficients[left_index + right_index] += left * right
        return Cyclotomic(coefficients)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Cyclotomic([value / scalar for value in self.coefficients])

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError('Use nonnegative integer powers')
        result = Cyclotomic([1])
        for unused in range(exponent):
            result *= self
        return result

    def __eq__(self, other):
        return self.coefficients == self.coerce(other).coefficients

    def conjugate(self):
        inverse_root = Cyclotomic([0, 1]) ** 9
        return sum(coefficient * inverse_root ** degree for degree, coefficient in enumerate(self.coefficients))


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


class Biquadratic:
    def __init__(self, coefficients=()):
        values = [Fraction(value) for value in coefficients]
        require(len(values) <= 4, 'biquadratic coefficient count')
        self.coefficients = tuple(values + [Fraction(0)] * (4 - len(values)))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Biquadratic) else Biquadratic([value])

    def __add__(self, other):
        other = self.coerce(other)
        return Biquadratic([left + right for left, right in zip(self.coefficients, other.coefficients)])

    __radd__ = __add__

    def __neg__(self):
        return Biquadratic([-value for value in self.coefficients])

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        values = [Fraction(0)] * 4
        for left_index, left in enumerate(self.coefficients):
            for right_index, right in enumerate(other.coefficients):
                common = left_index & right_index
                factor = (-3 if common & 1 else 1) * (-6 if common & 2 else 1)
                values[left_index ^ right_index] += left * right * factor
        return Biquadratic(values)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Biquadratic([value / scalar for value in self.coefficients])

    def __eq__(self, other):
        return self.coefficients == self.coerce(other).coefficients

    def conjugate(self):
        return Biquadratic([value * (1 if index in (0, 3) else -1)
                            for index, value in enumerate(self.coefficients)])


def rational_example():
    imaginary_three = Biquadratic([0, 1])
    imaginary_six = Biquadratic([0, 0, 1])
    omega = (-1 + imaginary_three) / 2
    phase_left = -(1 + 3 * imaginary_three) * (1 + imaginary_six) / 14
    phase_right = -(1 + 3 * imaginary_three) * (1 - imaginary_six) / 14
    phases = [[1, 1, 1, 1], [1, omega, phase_left, phase_right],
              [1, omega, phase_right, phase_left]]
    phases = [[Biquadratic.coerce(value) for value in row] for row in phases]
    point = [Fraction(1, 6), Fraction(1, 4), Fraction(7, 24), Fraction(7, 24)]
    residual = [1 - 3 * value for value in point]
    require(sum(point) == 1 and all(0 < value < Fraction(1, 3) for value in point), 'rational interior')
    for row in phases:
        require(all(value.conjugate() * value == 1 for value in row), 'rational unit phases')
    for row_index, row in enumerate(phases):
        for column_index, column in enumerate(phases):
            require(sum(weight * left.conjugate() * right
                        for weight, left, right in zip(point, row, column))
                    == int(row_index == column_index), 'rational weighted Gram matrix')
    pairings = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
    gaps = [residual[first] * residual[second] - residual[third] * residual[fourth]
            for first, second, third, fourth in pairings]
    require(gaps == [Fraction(7, 64), Fraction(1, 32), Fraction(1, 32)], 'rational pairing differences')
    for first, second, third, fourth in itertools.permutations(range(4)):
        require(residual[first] * residual[fourth] != residual[second] * residual[third],
                'rational permutation obstruction')
    require(min(abs(value) for value in gaps) / 6 == Fraction(1, 192), 'rational distance bound')
    return {'arithmetic': 'Q[u,v]/(u^2+3,v^2+6), u=i*sqrt(3), v=i*sqrt(6)',
            'diagonal': [str(value) for value in point],
            'residual': [str(value) for value in residual],
            'weighted_gram_matrix': [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            'pairing_differences': [str(value) for value in gaps],
            'excluded_permutations': 24, 'strict_interior': True,
            'total_variation_lower_bound': '1/192', 'status': 'pass'}


def family_polynomials():
    def constant(value):
        return {(0, 0, 0): Fraction(value)} if value else {}

    def addition(left, right):
        result = dict(left)
        for powers, coefficient in right.items():
            result[powers] = result.get(powers, 0) + coefficient
        return {powers: value for powers, value in result.items() if value}

    def multiplication(left, right):
        result = {}
        for left_powers, left_value in left.items():
            for right_powers, right_value in right.items():
                powers = tuple(left_power + right_power for left_power, right_power
                               in zip(left_powers, right_powers))
                result[powers] = result.get(powers, 0) + left_value * right_value
        return {powers: value for powers, value in result.items() if value}

    centre, radial, edge = [{powers: Fraction(1)} for powers in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    one_minus_edge = addition(constant(1), multiplication(constant(-1), edge))
    first = addition(centre, multiplication(constant(3), multiplication(radial, one_minus_edge)))
    second = addition(centre, multiplication(constant(3), multiplication(radial, edge)))
    residual = [first, second, centre, centre]
    main_gap = addition(multiplication(constant(3), multiplication(centre, radial)),
                        multiplication(constant(9), multiplication(multiplication(radial, radial),
                                       multiplication(edge, one_minus_edge))))
    other_gap = multiplication(constant(3), multiplication(multiplication(centre, radial),
                                 addition(constant(1), multiplication(constant(-2), edge))))
    for indices, expected in zip(((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)),
                                 (main_gap, other_gap, other_gap)):
        first_index, second_index, third_index, fourth_index = indices
        actual = addition(multiplication(residual[first_index], residual[second_index]),
                          multiplication(constant(-1), multiplication(residual[third_index], residual[fourth_index])))
        require(actual == expected, 'family coefficient identity')
    return {'arithmetic': 'Exact sparse rational polynomials in c,t,s',
            'pairing_differences': ['3*c*t+9*t^2*s*(1-s)', '3*c*t*(1-2*s)', '3*c*t*(1-2*s)'],
            'status': 'pass'}


def main():
    root = Cyclotomic([0, 1])
    radical = 2 * (root + root.conjugate()) - 1
    golden = (1 + radical) / 2
    alpha = (5 - radical) / 10
    beta = alpha / 2
    gamma = (radical - 1) / 4
    point = [alpha, beta, alpha, gamma]
    residual = [1 - 3 * value for value in point]
    phases = [[1, 1, 1, 1], [1, root ** 2, root ** 4, root ** 7], [-1, root ** 9, root ** 3, root ** 9]]
    phases = [[Cyclotomic.coerce(value) for value in row] for row in phases]
    require(root ** 5 == -1 and root ** 10 == 1, 'root powers')
    require(root.conjugate() * root == 1, 'unit root')
    require(radical ** 2 == 5 and radical.conjugate() == radical, 'real radical')
    require(golden ** 2 == golden + 1, 'golden identity')
    require(root ** 2 == golden * root - 1, 'quadratic phase relation')
    require(sum(point) == 1 and sum(residual) == 1, 'normalizations')
    require(alpha == 2 * beta, 'weight identity one')
    require(alpha * golden == beta + gamma, 'weight identity two')
    require((gamma - beta) * golden == alpha, 'weight identity three')
    lower, upper = Fraction(11, 5), Fraction(9, 4)
    require(0 < lower < upper and lower ** 2 < 5 < upper ** 2, 'positive radical interval')
    require(lower > 2 and upper < Fraction(7, 3), 'strict sign bounds')
    bounds = [(Fraction(5) - upper) / 10, (Fraction(5) - upper) / 20, (lower - 1) / 4]
    ceilings = [(Fraction(5) - lower) / 10, (Fraction(5) - lower) / 20, (upper - 1) / 4]
    require(all(value > 0 for value in bounds) and all(value < Fraction(1, 3) for value in ceilings), 'strict interior')
    for row in phases:
        require(all(value.conjugate() * value == 1 for value in row), 'unit phases')
    gram = []
    for row_index, row in enumerate(phases):
        gram_row = []
        for column_index, column in enumerate(phases):
            entry = sum(weight * left.conjugate() * right for weight, left, right in zip(point, row, column))
            expected = int(row_index == column_index)
            require(entry == expected, 'weighted Gram entry')
            gram_row.append(expected)
        gram.append(gram_row)
    pairings = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
    expected_differences = [(21 - 9 * radical) / 10, (33 - 15 * radical) / 40, -(21 - 9 * radical) / 10]
    for pairing, expected in zip(pairings, expected_differences):
        first, second, third, fourth = pairing
        actual = residual[first] * residual[second] - residual[third] * residual[fourth]
        require(actual == expected and actual != 0, 'exact pairing difference')
    for permutation in itertools.permutations(range(4)):
        first, second, third, fourth = permutation
        require(residual[first] * residual[fourth] != residual[second] * residual[third], 'permutation obstruction')
    require(117 - 51 * upper > 0 and 15 * lower - 33 == 0, 'distance gap ordering and lower bound')
    print(json.dumps({
        'arithmetic': 'Exact rational arithmetic in Q[z]/(z^4-z^3+z^2-z+1), z=exp(pi*i/5)',
        'weighted_gram_matrix': gram,
        'diagonal': ['(5-sqrt(5))/10', '(5-sqrt(5))/20', '(5-sqrt(5))/10', '(sqrt(5)-1)/4'],
        'pairing_differences': ['(21-9*sqrt(5))/10', '(33-15*sqrt(5))/40', '-(21-9*sqrt(5))/10'],
        'excluded_permutations': 24,
        'strict_interior': True,
        'total_variation_lower_bound': '(15*sqrt(5)-33)/240',
        'rational_example': rational_example(),
        'family_polynomials': family_polynomials(),
        'coverage': 'Exact Gram matrices and 24 orderings for each explicit diagonal, and family polynomial identities; the geometric conclusions, parameter-wide existence and rank-one criterion have written proofs in note.tex.',
        'status': 'pass'
    }, indent=2))


if __name__ == '__main__':
    main()
