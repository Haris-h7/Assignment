# Function:
# @decorator
# def capitalize_func(&lt;string&gt;):
# pass
# Sample input:
# result = capitalize_func(“test”)
# SampleOutput:
# TEST


def decorator(fun):

    def wrapper(S):
        Cap=S.upper()
        return fun(Cap)
    return wrapper


@decorator
def capitalize_fun(S):
    return S

print(capitalize_fun("test"))



