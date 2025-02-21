from tkinter.ttk import Button, Frame, Label, Entry, Combobox
from tkinter import Tk, messagebox, StringVar

from app.utils import validate_entry_char, validate_only_numbers, error_handler
from ..models import Pacient, session, GenderEnum


class PacientDataFrame(Frame):
    def __init__(self, parent: Tk, controller):
        super().__init__(parent)
        self.controller = controller

        validate_command_char = (self.register(validate_entry_char), "%S")
        validate_number = (self.register(validate_only_numbers), "%S")

        self.name_field = self._register_label_entry(
            text="Nombre: ",
            row=0,
            validatecommand=validate_command_char,

        )
        self.last_name_field = self._register_label_entry(
            text="Apellido: ", row=1, validatecommand=validate_command_char
        )
        self.bike_name = self._register_label_entry(
            text="Bicicleta: ", row=2, validatecommand=validate_command_char
        )
        self.age = self._register_label_entry(
            text="Edad (años): ", row=3, validatecommand=validate_number
        )
        self.weight = self._register_label_entry(
            text="Peso (kg): ", row=4, validatecommand=validate_number
        )
        self.height = self._register_label_entry(
            text="Altura (cm): ", row=5, validatecommand=validate_number
        )
        gender_label = Label(
            self, text="Sexo:"
        )  # solo permitira s
        self.gender = StringVar()
        gender_selector = Combobox(self, textvariable=self.gender, width=30, values=("Masculino", "Femenino"))
        gender_label.grid(row=6, column=0)
        gender_selector.grid(row=6, column=1, pady=5)
        # gender = self._register_label_entry(text="Genero: ", row=1, validatecommand=validate_command_char)

        # boton3 =  Button(self, text = "Enviar", command = textoDelCuadro)
        # boton4 =  Button(self, text = "Siguiente", width = 20, height = 5, command = CambiarVentanaAnalisis)
        # boton3.place(x = 250, y =150)
        # self.pack(fill='both', expand=1)
        # self.grid(row=0, column=0)
        save_pacient_btn = Button(
            self,
            text="Guardar paciente",
            width=20,
            command = lambda: self._save_new_pacient()
        )
        save_pacient_btn.grid(row=7, column=0, columnspan=2)
    @error_handler
    def _register_label_entry(self, row, text, validatecommand, validate="key", pady=5, **options):
        label = Label(self, text=text)
        entry = Entry(self, validate=validate, validatecommand=validatecommand)
        label.grid(row=row, column=0,pady=5,**options)
        entry.grid(row=row, column=1,pady=5,**options)
        return entry
    
    @error_handler
    def _validate_entry(self):
        entries : list[str] = [
            {"value":self.name_field.get(), "label" : "Nombre"},
            {"value":self.last_name_field.get(), "label": "Apellido"},
            {"value":self.bike_name.get(), "label": "Bicicleta"},
            {"value":self.age.get(), "label": "Edad"},
            {"value":self.weight.get(), "label": "Peso"},
            {"value":self.height.get(), "label": "Altura"},
            {"value":self.gender.get(), "label": "Genero"},
        ]
        for entry in entries:
            entry_value = entry["value"]
            entry_label = entry["label"]
            if not entry_value.strip():
                messagebox.showerror("Error", f"El campo {entry_label} es obligatorio",)
                return False
        return True
    
    @error_handler            
    def _save_new_pacient(self):
        if self._validate_entry():
            pacient = Pacient(
                name=self.name_field.get(),
                last_name=self.last_name_field.get(),
                bike_name=self.bike_name.get(),
                age=int(self.age.get()),
                weight=int(self.weight.get()),
                height=int(self.height.get()),
                gender = GenderEnum(self.gender.get())
            )
            session.add(pacient)
            session.commit()
            self.controller.current_pacient = pacient
            # self.controller.show_frame("NextFrame")
            # messagebox.showinfo("Paciente creado", f"El paciente {pacient.name} ha sido creado")
