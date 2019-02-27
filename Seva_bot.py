def Seva_bot(history,index,table):
	from random import choice as ch
	if index == 0:
		ei = 1
	else:
		ei = 0
	if len(history) == 0:
		return ch([True,False])
	eh = [history[i][ei] for i in range(len(history))]
	me = sum(eh)/len(eh)
	return me>0.5