from types import UnionType
from typing import Any
import math
from time import time


class a:
    count = 0

    def __init__(self) -> None:
        a.count += 1

    def __str__(self):
        return str(a.count)

    def __eq__(self, __value: object) -> bool:
        return self.count

    def __or__(self, __value: Any) -> UnionType:
        return self.count


#### Decorators #####

s = a(count=134)
print(a)
def monitor_time(f):
    def wrapper(*args):
        start = time()
        f(*args)
        end = time()
        print(f"time to calculate the factorial: ", end - start)

    return wrapper


@monitor_time
def calculation(nums):
    print(math.factorial(nums))

# calculation(10000)