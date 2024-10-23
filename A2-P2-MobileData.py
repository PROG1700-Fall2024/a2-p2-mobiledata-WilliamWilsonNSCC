#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:w0457754
#Student Name: William Wilson

def main():
    #0-200Mb $20 flat rate
    #200-500Mb $0.105 per Mb
    #500Mb - 1Gb (1000Mb) $0.110 per Mb
    #1Gb+ $118.00 flat rate

    #welcome message
    print("Welcome to Erewhon Mobile. I am Agent William. In order to help you better, can I get you to enter your data usage.")

    #gather data usage form client
    dataUsage = int(input("Enter data usage (MB): "))

    #break down data usage and cost 
    if dataUsage <= 200:
        ratePrice = 20
    elif dataUsage == 201 or dataUsage <= 500:
        ratePrice = dataUsage * 0.105
    elif dataUsage == 500 or dataUsage <=1000:
        ratePrice = dataUsage * 0.110
    else:
        ratePrice = 118

    #display to client the price for data usage
    print("Your total charge for data usage is: ${0:.2f}".format(ratePrice))

main()