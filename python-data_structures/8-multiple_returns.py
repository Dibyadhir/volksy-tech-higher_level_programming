#!/usr/bin/python3
def multiple_returns(sen):
    if len(sen) == 0:
        return None
    else:
        return len(sen), sen[0]
