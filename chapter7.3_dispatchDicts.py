def my_dict(x, y):
    return {
            'add' : operator.add(x, y),
            'sub' : operator.sub(x, y),
            'mul' : operator.mul(x, y),
            }
            
def dispatch(operator, x, y):
    return my_dict(x, y).get(operator, lambda: None)
    
print (dispatch('mul', 5, 2))
