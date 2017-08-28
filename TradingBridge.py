
# coding: utf-8

# In[ ]:

import pywaves as pw

WavesWalletID = "XXX-Finamatrix_Wallet_ID-XXX"
# Set Matcher node to use
pw.setMatcher(node = 'http://127.0.0.1:6886')

# set an address with a public key
WavesAddress = pw.Address(privateKey = 'CsBpQpNE3Z1THNMS9vJPaXqYwN9Hgmhd9AsAPrM3tiuJ')

# Asset names can be found at http://dev.pywaves.org/assets/
WavesAssetsIDs = { 'BTC' : '8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS',
                   'USD' : '4Aw6NnmkAELqK6FqQVj5nYB5PPt39TSccpFhgFKNYVAQ',
                   'FIX' : 'GS5RfWDS8ytVnxqr7M2pnqeFuu7BpSwGnADTcw23FvbZ'}

def FinamatrixBlackBox():
    ########################
    #     Confidential     #
    ########################
    ######Examplar Variable Setting######
    TokenPairNames = ["BTC","USD"]
    OrderType="long"
    OrderAmount=100000000
    Exchange="Waves"
    return(TokenPairNames, OrderType, OrderAmount, Exchange)

# Non-stop while loop: Whenever trading signal is triggred, execute trades 
# at the exchange with the trading amount and the selected assetpair provided by the signal
while(True):
    TokenPairNames, OrderType, OrderAmount, Exchange = FinamatrixBlackBox();
    if Exchange == "Waves":
        # post a buy order
        Asset1 = pw.Asset(TokenPairNames[0])
        Asset2 = pw.Asset(TokenPairNames[1])
        AssetPair = pw.AssetPair(Asset1, Asset2)
        if OrderType=="long":
            myOrder = WavesAddress.buy(assetPair = AssetPair, amount = OrderAmount, price = 1)
        elif OrderType=="short":
            myOrder = WavesAddress.sell(assetPair = AssetPair, amount = OrderAmount, price = 1)

