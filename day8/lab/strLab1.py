def myemail_info(email):
    if not "@" in email:
        return None
    first,second=email.split("@")
    return(first,second)

a=myemail_info("Aaa@123a")
print(a)

a=myemail_info("Asq@121aaa3a")
print(a)

a=myemail_info("Aaa123a")
print(a)