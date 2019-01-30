# import l3t1 as MODULE
# import l2t5 as MODULE
import l4t2 as MODULE
import sys


def get_local_objects(obj: object) -> list:
    # print(f"variables: {', '.join(objs)} in {MODULE} found")
    return [_obj for _obj in dir(obj) if not _obj.startswith("__")]


def get_full_size(x: object) -> int:
    spam = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                spam += get_full_size(item)
    elif hasattr(x, '__call__'):
        print(f"{x} can hide some variables, try memory_profile")
    return spam


def total_size(obj: object) -> int:
    eggs: int = 0
    for i in get_local_objects(obj):
        _obj = getattr(obj, i)
        _, obj_class, _ = str(type(_obj)).split("'")
        full_size = get_full_size(_obj)
        print(f"(var: {i}) \t (type: {obj_class}) \t (full size: {full_size})")
        eggs += full_size
    return eggs


if __name__ == "__main__":
    print(f"total size: {total_size(MODULE)}")
