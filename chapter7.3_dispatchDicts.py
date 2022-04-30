def my_dict(x, y):
    return {
            'add' : operator.add(x, y),
            'sub' : operator.sub(x, y),
            'mul' : operator.mul(x, y),
            }
            
def dispatch(operator, x, y):
    return my_dict(x, y).get(operator, lambda: None)
    
print (dispatch('mul', 5, 2))

## NOT SURE ABOUT THIS - It creates temporary dictionary everytime. For code to be fast, 
## create a dictionary once as a constant and then reference it when function is called.  
## How can I do that with x, y as parametres in the values
