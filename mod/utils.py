from mod.error import errors

def message(text):
    return {'message': text}

def status(text):
    if text == '' or text == None or text == {}:
        return {'status_code': '500', 'message': errors[500]}
    else:
        return {'status_code': '200'}