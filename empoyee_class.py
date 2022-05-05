import requests
class Employee:
    '''this is simple employee class'''
    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    #now let's have a look what mocking is
    def monthly_schedule(self,month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response'
            

