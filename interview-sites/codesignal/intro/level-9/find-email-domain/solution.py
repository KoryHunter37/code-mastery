# https://app.codesignal.com/arcade/intro/level-10/TXFLopNcCNbJLQivP

def findEmailDomain(address):
    domain_index = address.rfind('@')
    return address[domain_index+1:]
