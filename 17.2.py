def betweenab(func): 
 def _mydecorator(*args, **kw): 
  res = func(*args, **kw) 
  if res < a or res > b: 
   res = 1 
  return res 
 return _mydecorator 
 
 
@betweenab
def f(x): 
 return x*x - 5*x + 6
 
@betweenab
def f1(x,y): 
 return -1
