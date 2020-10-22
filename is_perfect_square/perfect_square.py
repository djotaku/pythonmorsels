import decimal
import cmath


def is_perfect_square(number, **kwargs):
    if kwargs.get("complex"):
        return (cmath.sqrt(number).real - int(cmath.sqrt(number).real) == 0) and (cmath.sqrt(number).imag - int(cmath.sqrt(number).imag) == 0)
    else:
        if number < 0:
            return False
        else:
            with decimal.localcontext() as c:
                c.prec = 100
                return decimal.Decimal(number).sqrt()-int(decimal.Decimal(number).sqrt()) == 0


if __name__ == "__main__":
    print(is_perfect_square(9))
    print(is_perfect_square(-9))
