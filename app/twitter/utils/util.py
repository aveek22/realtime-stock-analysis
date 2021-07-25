import json


def tuple_to_str(value):
    val = str(value)
    val = str.replace(val,'(','')
    val = str.replace(val,')','')
    val = str.replace(val,',','')
    val = str.replace(val,'\'','')
    return val