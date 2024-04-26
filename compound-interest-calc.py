#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
这是一个复利计算器。能够帮助大家方便、快速地计算不同储蓄方案在复利情况下n年后的收益。
This is a compound interest calculator. It can help everyone conveniently and quickly calculate the returns of different savings plans after n years under compound interest.
Github: https://github.com/Chiaki2333/compound-interest-calc
version: 1.0
'''
import os

# 将%形式的利率转化为float
def rate_change(rate):
    if "%" == rate.replace(" ","").replace("\t","").replace("\r","").replace("\n","")[-1]:
        return float(rate.replace(" ","").replace("\t","").replace("\r","").replace("\n","").replace("%","")/100.0
    else:
        return float(rate)

# 趸存Bulk/One-time deposit
def bulk(principal, rate, years):
    return float(principal)*pow(1+float(rate),float(years))
    
# 月存/Monthly deposit
def monthly_deposit_(init_principal, monthly_deposit, rate, months):
    months = int(months)
    money = init_principal
    for i in range(months):
        money += float(monthly_deposit)
        money += money*rate/12
    return money
    

# 年存/Annual deposit
def annual_deposit_(init_principal, annual_deposit, rate, years):
    years = float(years)
    money = init_principal
    for i in range(int(years)):
        money += float(annual_deposit)
        money += money*rate
    if float(years)-int(years) > 0:
        money = bulk(money, rate, float(years)-int(years))
    return money

if __name__== "__main__":
    print("\n".join([
        "    **       **",
        "  ******   ******",
        "  ***************",
        "    ***********",
        "      *******\tVersion:1.0",
        "        ***\tGithub:https://github.com/Chiaki2333/compound-interest-calc"
    ]))
    print("-"*50)
    print("This is a compound interest calculator. It can help everyone conveniently and quickly calculate the returns of different savings plans after n years under compound interest.")
    print("[1]One-time deposit")
    print("[2]Monthly deposit")
    print("[3]Annual deposit")
    choice = int(input("[*]Please choose:"))
    print("-"*50)
    if choice == 1:
        print("You choose [1]One-time deposit")
        print("Please input your principal, the deposit interest rate and how many years do you want to save.")
        principal = -1
        while principal<0:
            principal = float(input("[*]Your principal:"))
        rate = rate_change(input("[*]The deposit interest rate:"))
        years = -1
        while years<0:
            years = float(input("[*]how many years do you want to save:"))
        money = bulk(principal, rate, years)
        print("[!]You will get %.2f after %.2f year(s)." % (money, years))
    elif choice == 2:
        print("You choose [2]Monthly deposit")
        print("Please input your init principal, monthly deposit, the deposit interest rate and how many years do you want to save.")
        init_principal = -1
        while init_principal<0:
            init_principal = float(input("[*]Your init principal:"))
        monthly_deposit = -1
        while monthly_deposit<0:
            monthly_deposit = float(input("[*]Your monthly deposit:"))
        rate = rate_change(input("[*]The deposit interest rate:"))
        years = -1
        while years<0:
            years = float(input("[*]how many years do you want to save:"))
        money = monthly_deposit_(init_principal, monthly_deposit, rate, int(years*12))
        print("[!]You will get %.2f after %.2f year(s)." % (money, int(years*12)/12.0))
    elif choice == 3:
        print("You choose [3]Annual deposit")
        print("Please input your init principal, annual deposit, the deposit interest rate and how many years do you want to save.")
        init_principal = -1
        while init_principal<0:
            init_principal = float(input("[*]Your init principal:"))
        annual_deposit = -1
        while annual_deposit<0:
            annual_deposit = float(input("[*]Your annual deposit:"))
        rate = rate_change(input("[*]The deposit interest rate:"))
        years = -1
        while years<0:
            years = float(input("[*]how many years do you want to save:"))
        money = annual_deposit_(init_principal, annual_deposit, rate, years)
        print("[!]You will get %.2f after %.2f year(s)." % (money, years))
    os.system("pause")



