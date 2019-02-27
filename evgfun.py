def evgfun(history, num, table):
    
    def get_prob(des):
        prob = 0
        turns_amount = 0
        for turn in history:
            if (turn[num] == des):
                prob += turn[not num]
                turns_amount += 1
        if (turns_amount != 0):
            return (prob / turns_amount)
        return 1

    def count_exp(des):
        return (get_prob(des) * (table[des][1][0] - table[des][1][1]) + (1 - get_prob(des)) * (table[des][0][0] - table[des][0][1]))
    
    return count_exp(1) > count_exp(0)
