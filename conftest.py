import pytest
import time
from lib.tools.log import log


def pytest_sessionstart(session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    #print("X" * 100)
    #print("pytest_runtest_makereport", item)
    #print("X" * 100)
    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session, exitstatus):
    #print('pytest_sessionfinish'+"X"*100)
    print('run status code:', exitstatus)
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    print(f'there are {passed_amount} passed and {failed_amount} failed tests')
    log.info(f'Passed {passed_amount}, Failed {failed_amount}')
    #print(session,exitstatus)

def pytest_report_teststatus(report, config):
    if report.when == "call":
        pass
        #print("duration reported immediately after test execution:", report.duration)
        #log.info(f'====== Speed  {report.duration} ======')



def pytest_terminal_summary(terminalreporter, exitstatus, config):
    for reps in terminalreporter.stats.values():
        for rep in reps:
            if rep.when == "call":
                print("duration reported after all tests passed:", rep.nodeid,rep.duration)
                #log.info(f'====== Speed  {rep.duration} ======')

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    try:
        duration = time.time() - terminalreporter._sessionstarttime
        log.info(f'====== Speed  {format(duration, ".2g")} ======')
        print('duration:', duration, 'seconds')
        print('passed amount:', len(terminalreporter.stats['passed']))
        print('failed amount:', len(terminalreporter.stats['failed']))
        #print('xfailed amount:', len(terminalreporter.stats['xfailed']))
        #print('skipped amount:', len(terminalreporter.stats['skipped']))


    except:
        pass