from typing import Any, Callable, List, TypeVar, Iterable, MutableMapping
import funcy as f

T = TypeVar("T")

def test_typing_basics():
    # Test lmap with basic function
    res1: List[int] = f.lmap(lambda x: x * 2, [1, 2, 3])
    
    # Test lmap with None (identity)
    res2: List[int] = f.lmap(None, [1, 2, 3])
    
    # Test filter
    res3: Iterable[int] = f.filter(lambda x: x > 1, [1, 2, 3])
    
    # Test first
    res4: int | None = f.first([1, 2, 3])
    
    # Test walk on dict
    res5: MutableMapping[str, int] = f.walk(lambda item: (item[0], item[1] + 1), {"a": 1})

    # Test merge
    res6: MutableMapping[str, int] = f.merge({"a": 1}, {"b": 2})

if __name__ == "__main__":
    test_typing_basics()
