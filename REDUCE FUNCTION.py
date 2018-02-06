#REDUCE
from functools import reduce
result=list(reduce(lambda x,y:x+y,[47,11,42,13]))
print(result)