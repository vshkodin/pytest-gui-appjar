import pytest
from lib.tools.log import log
from lib.tools.cleanReports import clean_report

def test_runner(*args):
    clean_report()
    log.info(f'test run {args}')
    if len(args)==0:
        print("I AM IN ONE")
        print(args)
        pytest.main(['--alluredir=reports'])
    else:
        l=['--alluredir=reports']+args[0]
        pytest.main(l)