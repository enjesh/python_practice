tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print (tel)

print (tel['jack'])

del tel['sape']
tel['irv'] = 4127
print (tel)

print (list(tel))

print (sorted(tel))

print ('guido' in tel)

print ('jack' not in tel)