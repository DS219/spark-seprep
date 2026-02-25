def defang(ip):
    address = ""
    for part in ip:
        if part == ".":
            address += "[.]"
        else:
            address += part
    return address

#test cases
print(defang("1.1.1.1"))
print(defang("255.100.50.0"))