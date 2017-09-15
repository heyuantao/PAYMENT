# -*- coding: utf-8 -*-
from alipay import AliPay, ISVAliPay

def main():
    alipay = AliPay(appid="",app_notify_url="",app_private_key_path="./keys/priv2.txt",alipay_public_key_path="./keys/pub2.txt",\
                    sign_type = "RSA",debug = False )
    print alipay
    subject = u"测试订单".encode("utf8")
    # Pay via Web，open this url in your browser: https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(\
        out_trade_no="20161112",\
        total_amount=0.01,\
        subject=subject,\
        return_url="http://example.com",\
        notify_url="http://example.com/notify")
    print order_string
if __name__=="__main__":
    print "hello"
    main()