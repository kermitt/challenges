fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
celsius = {k:0.5555555555555556*(v-32) for (k,v) in fahrenheit.items()}

print(celsius)

celsius = {k:0.5555555555555556*(v-32) for (k,v) in fahrenheit.items() if v > -10 }
print(celsius)
## 
nested_dict = {'first':{'a':11, 'x':22, 'y':33, 'z':44}, 'second':{'b':2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)
for fd in float_dict:
    print(" ... ")
    for thing in float_dict[fd]:
        print("{} {} ".format( fd, thing) )
