def get_results():
    with open("guiLog.log") as f:
        f = f.readlines()
    return f[-1]