from multiprocessing import Process
import os
def run_proc(name):
	print('this is a tsst of multiprocess %s (%s)...'  % (name,  os.getpid()))
if __name__=='__main__':
	print('parant process os %s' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('child process will start')
	p.start()
	p.join()
	print('child process end')