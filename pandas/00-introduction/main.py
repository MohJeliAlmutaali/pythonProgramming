import pandas 

mydataset = {
        'cars' : ["BMW", "Volvo", "Ford"],
        'passings' : [3,10,2]
        }

myvar = pandas.DataFrame(mydataset)
print(myvar)
