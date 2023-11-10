set_countries = {'col','mex','can'}

size = set_countries.__len__()
print(size)

set_countries.add('ven')
print(set_countries)

set_countries.update({'per','arg','bol'})
print(set_countries)

set_countries.remove('per')
print(set_countries)

set_countries.clear()
print(set_countries)