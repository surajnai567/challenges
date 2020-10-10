from paytmchecksum import PaytmChecksum

# initialize an Hash/Array
paytmParams = {}

paytmParams["MID"] = "YOUR_MID_HERE"
paytmParams["ORDERID"] = "YOUR_ORDER_ID_HERE"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "YOUR_MERCHANT_KEY")
print("generateSignature Returns:" + str(paytmChecksum))

