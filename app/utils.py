from tkinter import messagebox

def validate_only_numbers(entry:str):
    return entry.isdigit()

def validate_entry_char(text:str):
    caracteres_baneados = "!#$%&/()=?¡¨*][_:>°1234567890'¿´+}{.-,<*-+°¬\~^`}´´¿´}]|"
    if text in caracteres_baneados or text == '"':
        return False
    return True

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    return wrapper
