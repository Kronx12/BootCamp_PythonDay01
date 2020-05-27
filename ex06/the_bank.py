class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
            Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        c_1 = False
        c_2 = False
        tmp_amount = 0
        account_1 = None
        account_2 = None
        if isinstance(origin, int) or isinstance(origin, str):
            if isinstance(dest, int) or isinstance(dest, str):
                for i in self.account:
                    if (isinstance(i, Account) and
                       ((i.id == origin or i.name == origin) or
                       (i.id == dest or i.name == dest)) and
                       len(i.__dict__) % 2 != 0):
                        tmp = 0
                        hasaddr = True
                        for attr in i.__dict__.keys():
                            if (attr[0] == 'b'):
                                self.fix_account(i)
                                return False
                            elif (attr == "name"):
                                tmp += 1
                            elif (attr == "id"):
                                tmp += 1
                            elif (attr == "value"):
                                tmp += 1
                            elif (attr.startswith('addr') or
                                  attr.startswith('zip')):
                                hasaddr = False
                        if (tmp != 3 or hasaddr):
                            if (i.id == dest or i.name == dest):
                                self.fix_account(dest)
                            else:
                                self.fix_account(origin)
                            return False
                        if (i.id == origin or i.name == origin):
                            c_1 = True
                            account_1 = i
                        if (i.id == dest or i.name == dest):
                            c_2 = True
                            account_2 = i
        if (c_1 and c_2):
            if (account_1.value >= amount):
                account_1.transfer(-amount)
                account_2.transfer(amount)
                return True
        return False

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        for i in self.account:
            tmp = 0
            hasaddr = True
            if (isinstance(i, Account) and
               (i.id == account or i.name == account)):
                if (len(i.__dict__) % 2 == 0):
                    i.__dict__.update("id", "name", "value", "zip", "addr")
                for attr in i.__dict__.keys():
                    if (attr[0] == 'b'):
                        attr[0] = attr[0][1:]
                        return False
                    elif (attr == "name"):
                        tmp += 1
                    elif (attr == "id"):
                        tmp += 1
                    elif (attr == "value"):
                        tmp += 1
                    elif (attr.startswith('addr') or attr.startswith('zip')):
                        hasaddr = False
                    if (tmp != 3 or hasaddr):
                        if (i.id == account or i.name == account):
                            i.__dict__.update("id", "name", "value",
                                              "zip", "addr")
                            return False
                    if (i.id == account or i.name == account):
                        c_1 = True
                        account_1 = i
