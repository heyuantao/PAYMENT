# -*- coding: utf-8 -*-
from alipay import AliPay, ISVAliPay

def main():
    alipay = AliPay(appid="2016081900287513",app_notify_url="",app_private_key_path="./keys/app_private.txt",alipay_public_key_path="./keys/alipay_public.txt",\
                    sign_type = "RSA2",debug = False )
    print alipay
    subject = u"技术支持服务".encode("utf8")
    # Pay via Web，open this url in your browser: https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(\
        out_trade_no="20161112",\
        total_amount=1,\
        subject=subject,\
        return_url="http://example.com",\
        notify_url="http://example.com/notify")

    gateWay = "https://openapi.alipaydev.com/gateway.do"
    print gateWay+"?"+order_string
if __name__=="__main__":
    print "hello"
    main()