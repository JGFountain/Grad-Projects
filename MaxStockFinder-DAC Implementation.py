def Best_Stock_finder(prices,l,m,h):
    lmax = m
    rmax = m+1
    sum_l = float('-inf')
    sum_r =float('-inf')
    total = 0


    for x in range(m, l -1 , -1):
        total += prices[x]
        if total > sum_l:
            sum_l = total
            lmax = x   

    for x in range(m +1, h +1 ):
        total += prices[x]
        if total > sum_r:
            sum_r = total
            rmax = x
    
    return rmax,lmax,sum_l + sum_r

def Find_max(prices,l,h):
    if h == l:
        return l, h, prices[l]
    else:
        mid = (l + h) //2
        l_low, l_high, l_sum = Find_max(prices,l,mid)
        r_low,r_high,r_sum = Find_max(prices,mid +1,h)
        c_low, c_high,cross =Best_Stock_finder(prices,l,mid,h)

        if l_sum >= r_sum and l_sum >= cross:
            return l_low, l_high,l_sum
        elif r_sum >= l_sum and r_sum >= cross:
            return r_low, r_high,r_sum
        else:
            return c_low,c_high,cross


import csv

def read_stocks(filename, symbol):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        prices = []
        dates = []
        for x in reader:
            if x[1] == symbol:
                dates.append(x[0])
                prices.append(float(x[3]))

        return prices, dates 
    
def deltas(d):
    return [d[i +1]- d[i] for i in range(len(d) -1)]

def company_name(filename):
    with open(filename,"r") as file:
        reader = csv.reader(file)
        next(reader)
        company={}
        for x in reader:
            symbol, name= x[0],x[1]
            company[symbol]= name
    
    return company


def main():
    company = company_name('securities.csv')
    max_profit = 0
    stock_optimum = ""
    opt_buy = ""
    opt_sell = ""

    for symbol in company.keys():
        prices,dates= read_stocks("prices-split-adjusted.csv",symbol)

        if not prices:
            continue

        delts = deltas(prices)
        if not delts:
            continue


        l,h,profit = Find_max(delts, 0 , len(delts)-1)
        if profit > max_profit:
            max_profit = profit
            stock_optimum=company[symbol]
            opt_buy=dates[l]
            opt_sell = dates[h]
    print(f'Best stock,{stock_optimum},{opt_buy},{opt_sell}')


if __name__== "__main__":
    main()