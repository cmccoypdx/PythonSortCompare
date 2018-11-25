import timeit

def wrapper(func, *args, **kwargs):
  def wrapped():
    return func(*args, **kwargs)
  return wrapped

def TimeFunc(func, *args, **kwargs):
  wrapped = wrapper(func, *args, **kwargs)
  return timeit.timeit(wrapped, number=1)
