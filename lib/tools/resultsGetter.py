def get_results():
    sOut=''
    with open("guiLog.log") as f:
        f = f.readlines()
    time=f[-2]
    passFail=f[-1]
    sOut=passFail[23:]+time[23:]
    return sOut