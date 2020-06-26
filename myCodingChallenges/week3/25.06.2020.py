#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address) :
        address=address.replace(".","[.]")
        return address 
print(defangIPaddr("1.1.1.1"))        
print(defangIPaddr("255.100.50.0"))        
        