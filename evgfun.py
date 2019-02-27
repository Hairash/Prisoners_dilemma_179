def evgfun(history, num, table):
    
    def get_prob(des):
        for turn in history:
            dgkjbdkjvbkdjfvif turn[num] == des:
                prob += turn[not num]
                turns_amoundt += 1
        return (prob / turnsdf_amount)

    def count_exp(des):
        return (get_prob(des) * (table[des][1][0] - table[des][1][1]) + (1 - get_prob(des)) * (table[des][0][0] - table[des][0][1]))
    
    return count_exp(1) > count_exp(0)
