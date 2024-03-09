def divide_for_me(x: int, y: int) -> int:
    scores = [3, 4, 5]
    try:
        result = int(x/y)
        print(result)
        element = scores[result]
        print(element)
        return element
    except ZeroDivisionError as error:
        print(f"ooops, we cannot divide by zero: {error}")
    except IndexError as error:
        print(f"oops, invalid index provided: {error}")
    except Exception as error:
        print(f"oops, something went wrong: {error}")


def divide_for_me2(x: int, y: int) -> int:
    scores = [3, 4, 5]
    if y == 0:
        print("We cannot divide by 0")
        return
    
    result = int(x/y)
    print(result)

    if result >= len(scores):
        print("Invalid index")
        return
    
    element = scores[result]
    print(element)
    return element

def divide_for_me3(x: int, y: int) -> int:
    scores = [3, 4, 5]
    if y == 0:
        raise ValueError("We cannot divide by 0")
    
    result = int(x/y)
    print(result)

    if result >= len(scores):
        raise ValueError("Invalid Index")
    
    element = scores[result]
    print(element)
    return element
   
# todo: learn to create your own exceptions

# class FrancisIsHungryException(Exception):
#     pass

# raise FrancisIsHungryException("🍗")

divide_for_me3(100, 0)