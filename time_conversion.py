import time

epoch = time.time() #Time in secons since 1970 Jan 1

def convert_epoch():
    seconds = round(epoch)            #Round to seconds
    minutes = round(seconds / 60)     #Converts seconds to minutes
    hours = round(minutes / 60)       #Convert minutes to hours
    days = round(hours / 24)          #Convert hours to days
    #Print out all the s,m,h,d since the epoch vvv
    print("seconds since the epoch: " + str(seconds))
    print("minutes since the epoch: " + str(minutes))
    print("hours since the epoch: " + str(hours))
    print("days since the epoch: " + str(days))



print("The current time and Date is: " + str(time.ctime()))
print("------------------------------------------------------")
convert_epoch()



