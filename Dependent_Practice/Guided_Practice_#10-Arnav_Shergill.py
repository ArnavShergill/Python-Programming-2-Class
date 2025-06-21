import formatting as f

f.title("Guided Practice #10")

f.dash()

f.section("Understanding *args")

def multiply(x, y):
    print(x*y)

multiply(5,4)

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4,5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)

f.dash()

f.section("Understanding **kwargs")

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(kwargs_1="Shark", kwargas_2=4.5, kwargs_3=True)

f.short_dash()

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Sammy", your_name = "Casey")

f.short_dash()

print_values(name_1="Alex", name_2 = "Gray", name_3 = "Harper", name_4 = "Phoenix", name_5 = "Remy", name_6 = "Val")

f.dash()

f.section("**kwarg Ordering Arguments")

def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

args = ("Sammy", "Casey", "Alex")
some_args(*args)

f.short_dash()

my_list = [2, 3]
some_args(1, *my_list)

f.short_dash()

def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)

kwargs = {"kwarg_1":"Val", "kwarg_2":"Harper", "kwarg_3":"Remy"}
some_kwargs(**kwargs)

f.dash()
