from tkinter.ttk import Button, Frame, Label, Entry
from tkinter import Tk, messagebox

from app.utils import validate_only_numbers
from ..models import Pacient, session


class SelectPacientFrame(Frame):
    def __init__(self, parent: Tk, controller):
        super().__init__(parent)
        self.controller = controller

        add_pacient_btn = Button(
            self,
            text="Nuevo paciente",
            width=20,
            command = lambda: controller.show_frame("PacientDataFrame"),
        )

        entry_label = Label(self, text="Ingrese ID del paciente")

        entry_pacient_id = Entry(
            self,
            validate="key",
            validatecommand=(self.register(validate_only_numbers), "%S")
            # validatecommand=(ventanaPaciente.register(validate_entry), "%S", "%P", 3)
        )

        select_paciente = Button(
            self,
            text="Ver informe del paciente",
            width=30,
            command=lambda: self._check_pacient_data(entry_pacient_id, controller),
        )

        # entradaIdPaciente.grid(row=2, column=0)
        # entradaTexto.grid(row=1, column=0)
        # boton1.grid(row=0, column=0, columnspan=2, padx=170, pady=50)
        # boton2.grid(row=1, column=1, rowspan=2)
        add_pacient_btn.pack(pady=50)
        entry_label.pack()
        entry_pacient_id.pack()
        select_paciente.pack(pady=50)

        # self.pack(fill='both', expand=1)
        # self.grid(row=0, column=0)


    def _check_pacient_data(self, pacient_id_entry:Entry, controller):
        if not pacient_id_entry.get():
            return messagebox.showerror("ID de usuario no especificado")
        
        pacient_id = int(pacient_id_entry.get())
        pacient : Pacient = session.query(Pacient).filter(Pacient.id==pacient_id).first()
        if pacient is not None:
            return controller.show_frame("NextFrame")
        messagebox.showerror("Usuario NO ENCONTRADO", f"El usuario con el id {pacient_id} no existe")
        