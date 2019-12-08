with file('input') as f:
    indata = f.read()

indata_list = indata.split('\n')
def get_fuel(x):
    try:
        fuel = int(x)/3-2
    except:
        print x
        fuel = 0
    return fuel
fuel_list = [get_fuel(e) for e in indata_list]

print fuel_list
print sum(fuel_list)
print "CORRECT"

print "Task 2:"
def get_fuel_recursive(x):
    try:
        if x <= 6:
            return 0
        fuel = int(x)/3-2
        fuel += get_fuel_recursive(fuel)
    except:
        print x
        fuel = 0
    return fuel

fuel_list_rec = [get_fuel_recursive(e) for e in indata_list]
print fuel_list_rec
print sum(fuel_list_rec)
