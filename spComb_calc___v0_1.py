# Series / Parallel combination calculator function
#
# Auxiliary function to calculate closest series and parallel combination of a given target value out of the pool of
# values corresponding to the given E-series of preferred values.
#
# See main Function: spComb_GUI for more info.
#
# Version: 0.1
#
# Author: Boris Jung
# Date: 22.03.2020
#
from decimal import Decimal, getcontext
from e_series_values import valMat
#
def calc_spc(Val, Series):
    # INPUT VALUES
    # replace with user input routine!!!
    targValue = Decimal('{}'.format(Val))
    targSer = '{}'.format(Series)
    print('Target Value: {} \nTarget Series: {}\n'.format(targValue, targSer))
#
    # Set e-Values List from 1 decades below to 1 decades above target value
    valuesMat = valMat(targSer,targValue.adjusted()-1,targValue.adjusted()+1)
#
    # Closest Value
    closestVal = Decimal('inf')
    for x in range(len(valuesMat)):
        if abs(min(valuesMat[x], key = lambda x: abs(x - targValue)) - targValue) < abs(closestVal - targValue):
            closestVal = min(valuesMat[x], key = lambda x: abs(x - targValue))
    print("Closest single value: {}\n".format(closestVal))
#
    # Closest combinations
    # NOTE: only finds the first of equally close pairs!
    tmpSerDev = Decimal('inf')
    tmpParDev = Decimal('inf')
    for m in range(len(valuesMat)):
        for n in range(len(valuesMat[0])):
            for i in range(len(valuesMat)): # TRY TO CHANGE INNER ROUTINE TO lambda AND COMPARE SPEEDS!
                for j in range(len(valuesMat[0])):
                    series = valuesMat[i][j] + valuesMat[m][n]
                    parallel = (valuesMat[i][j] * valuesMat[m][n])/(valuesMat[i][j] + valuesMat[m][n])
                    if abs(series-targValue) < tmpSerDev:
                        tmpSerDev = abs(series-targValue)
                        serVal1 = valuesMat[i][j]
                        serVal2 = valuesMat[m][n]
                    if abs(parallel-targValue) < tmpParDev:
                        tmpParDev = abs(parallel-targValue)
                        parVal1 = valuesMat[i][j]
                        parVal2 = valuesMat[m][n]
    closestDev = ((closestVal/targValue-1)*100).quantize(Decimal('1.00'))
    serComb = serVal1 + serVal2
    serDevPerc = ((serComb/targValue-1)*100).quantize(Decimal('1.00'))
    parComb = ((parVal1 * parVal2)/(parVal1 + parVal2)).quantize(Decimal('1.00'))
    parDevPerc = ((parComb/targValue-1)*100).quantize(Decimal('1.00'))
#
    print("Closest series combination: {} + {} = {}".format(str(serVal1),str(serVal2),str(serComb)))
    print("Deviation from Target Value: {}%\n".format(str(serDevPerc)))
#
    print("Closest parallel combination: {} + {} = {}".format(str(parVal1),str(parVal2),str(parComb)))
    print("Deviation from Target Value: {}%\n".format(str(parDevPerc)))

    vals_and_dev = {"cVal":closestVal, "cDev":closestDev,
                    "sVal1":serVal1, "sVal2":serVal2, "sComb":serComb, "sDev":serDevPerc,
                    "pVal1":parVal1, "pVal2":parVal2, "pComb":parComb, "pDev":parDevPerc}
    return vals_and_dev