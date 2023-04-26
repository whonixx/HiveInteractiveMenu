
import sys
import json
import subprocess
from SPLGenericHelperFunctions import *

#start of method definition
def menu():
    print("****** Select an Option ******")
    print("1. Start GLX Claiming/Staking script")
    print("2. Print Account Balances ")
    print("3. Sweep DEC from secondary accounts to main account ")
    print("4. test method 4")
    print("5. Exit")
    
    while True:
        choice = input("Please enter an option number ")
        if choice not in ("1", "2", "3","4","5"):
            print("that is not a valid option")
        else:
            break
    if choice == "1":
        method1()
        return False
    if choice == "2":
        method2(jsonAccounts)
        return False
    if choice == "3":
        method3()
        return False
    if choice == "4":
        method4()
        return False
    if choice == "5":
        return True

def method1():
    subprocess.Popen([sys.executable, 'GLXStakingScript.py'], creationflags = subprocess.CREATE_NEW_CONSOLE)

def method2(jsonAccounts):
    printAccountBalances(accMainName)
    printAccountBalances(acc2Name)
    printAccountBalances(acc3Name)
    printAccountBalances(acc4Name)

def method3():
    sweepTokensToMain(accMainName,acc2Name,acc2ActiveKey,tknDEC)
    sweepTokensToMain(accMainName,acc3Name,acc3ActiveKey,tknDEC)
    sweepTokensToMain(accMainName,acc4Name,acc4ActiveKey,tknDEC)

def method4():
    tokenTransfer(accMainName,accMainActiveKey,acc3Name,tknDEC[0],10)
    
    #h = Hive(keys=[jsonAccounts['accMainPostingKey'], jsonAccounts['accMainActiveKey']])
    #a = Account(jsonAccounts['accMainName'], blockchain_instance=h)
    #print(a.get_account_bandwidth())
    #a.transfer('wobs', '0.001', 'HIVE', memo= 'memo, Test transaction 2')

def loadAccounts():
    with open('keys.json') as user_file:
        jsonAccounts = json.load(user_file)
    return jsonAccounts

#var definition
_exit = False
jsonAccounts = loadAccounts()
accMainName = jsonAccounts['accMainName']
accMainPostingKey = jsonAccounts['accMainPostingKey']
accMainActiveKey = jsonAccounts['accMainActiveKey']
acc2Name = jsonAccounts['acc2Name']
acc2PostingKey = jsonAccounts['acc2PostingKey']
acc2ActiveKey = jsonAccounts['acc2ActiveKey']
acc3Name = jsonAccounts['acc3Name']
acc3PostingKey = jsonAccounts['acc3PostingKey']
acc3ActiveKey = jsonAccounts['acc3ActiveKey']
acc4Name = jsonAccounts['acc4Name']
acc4PostingKey = jsonAccounts['acc4PostingKey']
acc4ActiveKey = jsonAccounts['acc4ActiveKey']

print(accMainName + ' account keys successfully loaded')
print(acc2Name + ' account keys successfully loaded')
print(acc3Name + ' account keys successfully loaded')
print(acc4Name + ' account keys successfully loaded')

#main code to run
while _exit == False:
    _exit = menu()
    print("\n\n")