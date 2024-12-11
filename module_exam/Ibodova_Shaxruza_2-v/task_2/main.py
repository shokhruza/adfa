from datetime import datetime

datatime_ = "2009-02-12 21:37:58"
vaqt_obj = datetime.strptime(datatime_, "%Y-%m-%d %H:%M:%S")

second = (vaqt_obj - datetime(1970, 1, 1)).total_seconds()
print("Seconds:", int(second))
