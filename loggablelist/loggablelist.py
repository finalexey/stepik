import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, msg):
        super().append(msg)
        super().log(msg)


x = LoggableList()
# x.log("2121")
x.append("1231")
time.sleep(2)
x.append("5741")
time.sleep(2)
x.append("1421")
time.sleep(2)
x.append("3411")
x.append("4521")