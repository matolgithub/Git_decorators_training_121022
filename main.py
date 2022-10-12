# import time
#
#
# def degree_decorator(func):
#     start = time.time()
#
#     def wrapper(*args, **kwargs):
#         x = 'Hello'
#         result_degree_func = func(*args, **kwargs)
#         end = time.time()
#         total_time = end - start
#         print(f"{x} from decorator: {result_degree_func}...Total time: {total_time}")
#         return func
#     return wrapper
#
#
# @degree_decorator
# def degree_func(number):
#     result =  number ** 2
#     print(result)
#
#     return result
#
#
# degree_func(5)

def function_decorator(func):
    def wrapper(*args):
        func_list = func(*args)
        new_decor_list = [(str(item) + "odd") if item % 2 != 0 else (str(item) + "even") for item in func_list]
        print(f"NEW LIST: {new_decor_list}")

        return new_decor_list

    return wrapper


@function_decorator
def simple_function(num):
    num_list = [item for item in range(1, num + 1)]
    print(f"The previous list: {num_list}")
    return num_list


simple_function(10)
function_decorator(simple_function(20))
