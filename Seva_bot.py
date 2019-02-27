 def Seva_bot(history,index,table):
    if index == 0:
        ei = 1
    else:
    	ei = 0
    eh = [history[i][ei] for i in range(len(history))]
    me = sum(eh)/len(eh)
    return me>0.5