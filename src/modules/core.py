from .request import reqController
from .logger import logController


def coreController(list):
    urllist = list
    if urllist:
        for i in urllist:
            name = i[0]
            url = i[1]
            r = reqController(url)
            corePreLogger(n=name, u=url, s=r, err=checkError(r))
    else:
        errormsg = "INPUT IS EMPTY!!!!!!"
        corePreLogger(n=None, u=None, s=None, err=errormsg)

# TODO: CREATE PRELOG


def corePreLogger(n, u, s, err):
    logController()
    pass


def checkError(r):
    if not r:
        errormsg = "CONN ERROR"
        return errormsg
