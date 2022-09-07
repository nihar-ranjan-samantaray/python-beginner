files = ['20220829 - Indicator-Crypto (1).csv','20220829 - Indicator-Crypto-Binance.csv','20220829 - Indicator-Crypto.csv','20220829 - Indicator-ETF.csv','20220829 - Indicator-Futures-ALT.csv','20220829 - Indicator-Futures.csv','20220829 - Indicator-Stock.csv','20220829 - PriceMap-Crypto-Binance.csv','20220829 - PriceMap-Crypto-Web (1).csv','20220829 - PriceMap-Crypto-Web (2).csv','20220829 - PriceMap-Crypto-Web.csv','20220829 - PriceMap-ETF.csv','20220829 - PriceMap-Futures-ALL.csv','20220829 - PriceMap-Futures-All2.csv','20220829 - PriceMap-Futures-Web.csv','20220829 - PriceMap-Futures-Web2.csv','20220829 - PriceMap-Stocks.csv','20220829 - PriceMap_Bookmap_Binance.csv','20220829 - PriceMap_Bookmap_Kraken (1).csv','20220829 - PriceMap_Bookmap_Kraken.csv','20220829 - TEST3PriceMap-Crypto-Web.csv','20220829 - TEST6PriceMap_Bookmap_Kraken.csv','20220829 - TEST7Indicator-Crypto.csv']

newFiles = files
import re
popList = []
for eachFile in files:
    if '(' in eachFile:
        filename = re.search(r'(.*) \(', eachFile).group()
        duplicate_filename = filename.replace(' (','.csv')
        index = newFiles.index(duplicate_filename)
        popList.append(index)

print(popList)
uniquePopList=[*set(popList)]
for _ in uniquePopList:
    newFiles.pop(_)

print(newFiles)
