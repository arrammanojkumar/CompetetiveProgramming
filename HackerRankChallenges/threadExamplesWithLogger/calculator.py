#!/bin/python3

__author__ = "Manoj Kumar Arram"

pressureList = []

pressureList = [100, 120, 50, 170, 20, 10, 20, 10, 15, 25, 20, 20, 20, 25]

# 0 Initial case in which we get tY
# 1 It is inside boundary so ty=tCurrent
# 2 It is outside boundary so tCurrent one time then decrease with ty/tCurrent*deltaT
# 3 It is below p2 so find oneTime tCurrent and add with deltaT/beta*tY
prevCase = caseNo = 0
riskProbability = 0.95
presentation_mode = 'sleeping'
pressuremetric = 'pip'
P2 = None
tYBoundary = None


def getCase(sacrumPressure, P2, tYBoundary):
    caseNo = 0
    if P2 is None or tYBoundary is None:
        caseNo = 0
    elif tYBoundary[0] <= sacrumPressure <= tYBoundary[1]:
        caseNo = 1
    elif sacrumPressure > P2 and (sacrumPressure < tYBoundary[0] or sacrumPressure > tYBoundary[1]):
        caseNo = 2
    elif sacrumPressure < P2:
        caseNo = 3
    print("getCase sacrumPressure:", sacrumPressure, " P2:", P2, " tYBoundary:", tYBoundary, " caseNo:", caseNo)
    return caseNo


def risk_timer(pressureMetric, pressure, riskProbability, d=None, presenation_mode='sleeping'):
    return pressure * riskProbability


def calRisk(tY, risk_time, tYtCurrent, isDecrease):
    diff = 2 / 60
    beta = 15

    if isDecrease:
        return risk_time - (tYtCurrent * diff)
    else:
        return risk_time + ((diff / beta) * tY)

# 94.6380952309525+(((2/60)/15)*(95.0)), 97.8047618976
# tYBoundary = (80.0, 120.0)
# P2 = 30.0
# caseNo = 1
# getCase(70, P2, tYBoundary)


for pressure in pressureList:
    # If Initial Pressure is not there then we have to calculate TY
    sacrumPressure = pressure
    caseNo = getCase(sacrumPressure, P2, tYBoundary)
    print("sacrumPressure:", sacrumPressure, " prevCase:", prevCase, " caseNo:", caseNo)

    if caseNo == 0:
        Y = sacrumPressure
        risk_time = risk_timer(pressuremetric, pressure, riskProbability, None,
                               presentation_mode)
        tY = risk_time
        tYBoundary = (Y - Y * 0.20, Y + Y * 0.20)
        P2 = Y * 0.30
        prevCase = caseNo
        print("\t caseNo:", caseNo, ' risk_time:', risk_time, " tY:", tY)

    elif prevCase is not None and caseNo == 1:
        isDecrease = True
        if prevCase != caseNo:
            tCurrentPressure = tY
            tYtCurrent = tY / tCurrentPressure
        print("\t Before RiskTime : ", risk_time)
        risk_time = calRisk(tY, risk_time, tYtCurrent, isDecrease)
        print("\t caseNo:", caseNo, " tYtCurrent:", tYtCurrent, " tY:", tY, " tCurrentPressure:", tCurrentPressure,
              ' risk_time:',
              risk_time)

        prevCase = caseNo

    elif prevCase is not None and caseNo == 2:
        isDecrease = True
        if prevCase != caseNo:
            tCurrentPressure = risk_timer(pressuremetric, pressure, riskProbability, None,
                                          presentation_mode)
            tYtCurrent = tY / tCurrentPressure
        print("\t Before RiskTime : ", risk_time)
        risk_time = calRisk(tY, risk_time, tYtCurrent, isDecrease)
        print("\t caseNo:", caseNo, " tYtCurrent:", tYtCurrent, " tY:", tY, " tCurrentPressure:", tCurrentPressure,
              ' risk_time:',
              risk_time)
        prevCase = caseNo

    elif prevCase is not None and caseNo == 3:
        isDecrease = False
        if prevCase != caseNo:
            tCurrentPressure = risk_timer(pressuremetric, pressure, riskProbability, None,
                                          presentation_mode)
            tYtCurrent = tY / tCurrentPressure
        print("\t Before RiskTime : ", risk_time)
        isDecrease = False
        risk_time = calRisk(tY, risk_time, tYtCurrent, isDecrease)
        print("\t caseNo:", caseNo, " tYtCurrent:", tYtCurrent, " tY:", tY, " tCurrentPressure:", tCurrentPressure,
              ' risk_time:',
              risk_time)
        prevCase = caseNo
