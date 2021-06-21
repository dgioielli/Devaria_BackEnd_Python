from datetime import datetime


def validar_data(data, formatoData = "%Y-%m-%d"):
    try:
        print (data)
        data = datetime.strptime(str(data), formatoData)
        return data
    except Exception:
        return None