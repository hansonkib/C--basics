from time import clock
print('enter name')
start_time=clock()
name=input()
current_time=clock()
elapse=current_time-start_time
print('hey',name,"you took",elapse,"to think")
