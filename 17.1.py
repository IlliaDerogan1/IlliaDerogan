def module(func): 
 def _mydecorator(*args, **kw): 
  res = func(*args, **kw) 
  if res<0: 
   res = -res 
  elif res==0: 
   res = 1 
  return res 
 return _mydecorator 
 
@module
def f(x): 
 return x*x - 5*x + 6 
 
@module
def f1(x,y): 
 return -1
