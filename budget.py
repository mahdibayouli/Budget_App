def float_to_str(a):
    st = str(float(a))
    parts = st.split('.')
    parts[1] = parts[1].ljust(2, '0')[:2]
    st = parts[0]+'.'+parts[1]
    return st.rjust(7, ' ')

def percentages_vertical(percentages):
    result = ''
    line = ''
    for i in range(11):
        line = str(i*10).rjust(3,' ') + '| '
        for j in range(len(percentages)):
            if (percentages[j]>0):
                line += 'o  '
                percentages[j]-=10
            else:
                line += '   '
        result = line + '\n' + result
    return result
        
def categories_vertical(categories):
    result = ''.ljust(4,' ') + ''.ljust(1+ len(categories)*3 , '-') + '\n'
    line = ''
    index = 0
    while (line != ''.ljust(14,' ')):
        if(index>0):
            result += line + '\n'
        line = ''.ljust(5,' ')
        for category in categories:
            line += category.name[index:index+1].ljust(3,' ')
        index+=1
    return  result.rstrip('\n')
            
            
    
        


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = 0
        self.deposits = 0
        self.withdrawals = 0

    def deposit(self, amount, description=''):
        newdict = dict()
        newdict["amount"] = amount
        newdict["description"] = description
        self.ledger.append(newdict)
        self.balance += amount
        self.deposits += amount
        
    def withdraw(self, amount, description=''):
        newdict = dict()
        newdict["amount"] = -amount
        newdict["description"] = description
        if(self.check_funds(amount) == True):
            self.ledger.append(newdict)
            self.balance -= amount
            self.withdrawals += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if(self.check_funds(amount) == True):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if (amount > self.balance):
            return False
        else:
            return True

    def __str__(self):
        result = ''
        result += self.name.center(30,'*') + '\n'
        for dict in self.ledger:
            desc = dict['description'][:23].ljust(23,' ')
            amount = float_to_str(dict['amount'])
            result += desc + amount + '\n'
        result+= 'Total: ' + str(self.balance)
        return result


def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    percentages = list()
    total = 0 
    for category in categories:
        total += category.withdrawals
    for category in categories:
        percentage =  (float(category.withdrawals) / float(total)) * 100
        percentages.append(percentage)
    return result + percentages_vertical(percentages) + categories_vertical(categories)