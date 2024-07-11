from mypackage import *

print(public_function())

# try:
#     print(internal_function())
# except NameError as e:
#     print(e)

try:
    from mypackage import _internal_module
except ImportError as e:
    print(e)
