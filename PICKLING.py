grades={'harsh':75,'rishabh':80,'deepak':65}
import pickle
f=open('a.p','wb')
pickle.dump(grades,f)       # pickle file is newly created
f.close()                  #dump data to f

f=open('a.p','rb')       # r for reading ; can be omitted
mydict=pickle.load(f)

print(mydict)

