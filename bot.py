from logger import logger

############################################# CLASSES #############################################
class IndividualOrder:
    name = ""
    subtotal = 0.00
    tax = 0.00
    tip = 0.00
    fees = 0.00
    total = 0.00

class OverallOrder:
    subtotal = 0.00
    numOfOrders = 0
    orders = []
    tipAmount = 0.00
    taxTotal = 0.00
    taxRate = 0.00
    feesTotal = 0.00
    total = 0.00

############################################# MAIN #############################################
if __name__ == '__main__':
    def process():
        logger.writeLine("Process Starting...")

        OO = OverallOrder()
        #gather order info
        getOrderDetails(OO)

        # get tip amount for each individual
        individualTipAmount = divideAmountAmongOrders(OO.tipAmount, OO.numOfOrders)
        
        # get user to enter orderer names and subtotals
        orderNumber = 1
        for x in range(OO.numOfOrders):
            order = IndividualOrder()
            order.name = input("Enter the name for order number " + str(orderNumber) + ": ")
            order.subtotal = input("Enter " + order.name + "'s subtotal: ")
            order.tip = float(individualTipAmount)
            OO.subtotal = float(OO.subtotal) + float(order.subtotal)
            OO.orders.append(order)
            orderNumber += 1

        logger.writeLine("Order subtotal is: " + str(OO.subtotal))
        
        # get the tax rate
        OO.taxRate = calculateTaxRate(OO.taxTotal, OO.subtotal)
        # get the total fee amount
        OO.feesTotal = getOrderFees(OO)

        # set taxes and fees on individual orders, calculate and display user's total
        getIndividualTotals(OO)
        verifyIndividualsCoverOverallTotal(OO.orders, OO.total)
        revealIndividualTotals(OO.orders)

        logger.writeLine("Process complete!")


    def getOrderDetails(OO):
        OO.tipAmount = float(input("Enter the total tip amount: "))
        OO.taxTotal = float(input("Enter the total amount of taxes: "))
        OO.total = float(input("Enter the final order total amount: "))
        OO.numOfOrders = int(input("Enter number of orders: "))
        
    def divideAmountAmongOrders(totalAmount, numberOfOrders):
        return float(totalAmount) / float(numberOfOrders)

    def calculateTaxRate(taxTotal, subtotal):
        taxRate = float(taxTotal) / float(subtotal)
        logger.writeLine("Order tax rate is: " + str(taxRate))
        return taxRate
    
    def getOrderFees(OO):
        # leave line below for debugging
        # logger.writeLine("subtotal: " + str(OO.subtotal) + ". tipAmount: " + str(OO.tipAmount) + ". taxTotal: " + str(OO.taxTotal))
        subTipTax =  float(OO.subtotal) + float(OO.tipAmount) + float(OO.taxTotal)
        fees = float(OO.total) - float(subTipTax)
        logger.writeLine("Order fees: $" + str(fees))
        return fees
    
    def getIndividualTotals(OO):
        for o in OO.orders:
            o.tax = float(o.subtotal) * float(OO.taxRate)
            o.fees = divideAmountAmongOrders(OO.feesTotal, OO.numOfOrders)
            o.total = round(float(o.subtotal) + float(o.tip) + float(o.tax) + float(o.fees), 2)

    def verifyIndividualsCoverOverallTotal (orders, total):
        ordersTotal = 0.00
        for o in orders:
            ordersTotal = float(ordersTotal) + float(o.total)
        if ordersTotal == total:
            logger.writeLine("The sum of individual totals covers the total exactly!")
        elif ordersTotal < total:
            difference = float(total) - float(ordersTotal)
            logger.writeLine("The sum of individual totals is less than total by $" + str(difference) + ". Adding difference to first order.")
            orders[0].total = float(orders[0].total) + float(difference)
        else:
            difference = float(ordersTotal) - float(total)
            logger.writeLine("The sum of indvidual totals is more than total by $" + str(difference) + ". Subtracting difference to first order.")
            orders[0].total = float(orders[0].total) - float(difference)

    def revealIndividualTotals (orders):
        for o in orders:
            logger.writeLine(o.name + "'s total is: $" + str(o.total))

    ############################################# Kickoff process here #############################################
    process()