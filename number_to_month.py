# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if month < 1 or month > 12:
        return "error"
    else:
        return months[month-1]
