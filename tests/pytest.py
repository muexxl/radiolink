#! /usr/bin/env python
var = 5

def localfunction():
    global var
    print("Entering local function")
    print(f"Var is {var}")
    var = 4
    
def main():

    global var 
    print(f"Starting Main")
    localfunction()
    print(f"Var is {var}")
    
main()