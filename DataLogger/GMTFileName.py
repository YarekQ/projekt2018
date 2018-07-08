import time
def GMTFileName():
    """
    funkcja zwraca unikatowego stringa yyyymmddhhmmss używanego do kreowania unikalnych nazw plikow
    :return:
    """

    GMTLoggingStartTime = time.gmtime()
    GMTFileName = str(GMTLoggingStartTime[0]) + str(GMTLoggingStartTime[1]) + str(GMTLoggingStartTime[2]) + str(
        GMTLoggingStartTime[3]) + str(GMTLoggingStartTime[4]) + str(GMTLoggingStartTime[5])

    return G