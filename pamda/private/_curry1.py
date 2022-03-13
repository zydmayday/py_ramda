def _curry1(fn):
  def f1(*a):
    if len(a) == 0:
      return f1
    else:
      return fn(*a)
  return f1
