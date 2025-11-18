from typing import Protocol

#super classe de pessoas
class Person:    
    def __init__(self, name: str, email: str, id: str, phone: str):
        self._name = name
        self._email = email
        self._id = id
        self._phone = phone
    
    #getters
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def phone(self) -> str:
        return self._phone
    
    #setters
    @email.setter
    def email(self, new_email: str):
        self._email = new_email
    
    @phone.setter
    def phone(self, new_phone: str):
        self._phone = new_phone
    
    def __str__(self) -> str:
        return f"{self._name} | Email: {self._email} | Telefone: {self._phone}"

#classe dos donos dos pets  
class Client(Person):    
    def __init__(self, name: str, email: str, id: str, phone: str):
        #chama o construtor da classe pai
        super().__init__(name, email, id, phone)
    
    def __str__(self) -> str:
        return f"Cliente: {super().__str__()}"

#classe dos veterinários
class Veterinarian(Person):
    def __init__(self, name: str, email: str, id: str, phone: str, specialty: str):
        super().__init__(name, email, id, phone)
        self._specialty = specialty
    
    @property
    def specialty(self) -> str:
        return self._specialty
    
    @specialty.setter
    def specialty(self, new_specialty: str):
        self._specialty = new_specialty
    
    def __str__(self) -> str:
        return f"Veterinário: {super().__str__()} | Especialidade: {self._specialty}"

#classe pets
class Pet:
    def __init__(self, name: str, species: str, age: int, owner: Client):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__owner = owner
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def species(self) -> str:
        return self.__species
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def owner(self) -> Client:
        return self.__owner
    
    @age.setter
    def age(self, new_age: int):
        if new_age >= 0:
            self.__age = new_age
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__species}, {self.__age} anos) - Dono: {self.__owner.name}"
    
#classe abstrata de consultas
class Appointment:
    def __init__(self, pet: Pet, veterinarian: Veterinarian, date: str):
        self._pet = pet
        self._veterinarian = veterinarian
        self._date = date
        self._status = "Agendada"
    
    @property
    def pet(self) -> Pet:
        return self._pet
    
    @property
    def veterinarian(self) -> Veterinarian:
        return self._veterinarian
    
    @property
    def date(self) -> str:
        return self._date
    
    @property
    def status(self) -> str:
        return self._status
    
    @status.setter
    def status(self, new_status: str):
        self._status = new_status
    
    def get_price(self) -> float:
        return 0.0
    
    def get_type(self) -> str:
        return "Consulta"
    
    def __str__(self) -> str:
        return (f"{self.get_type()} - Pet: {self._pet.name} | "
                f"Veterinário: {self._veterinarian.name} | "
                f"Data: {self._date} | Status: {self._status} | "
                f"Valor: R$ {self.get_price():.2f}")

#consulta de rotina
class RoutineAppointment(Appointment):
    def __init__(self, pet: Pet, veterinarian: Veterinarian, date: str):
        super().__init__(pet, veterinarian, date)
    
    def get_price(self) -> float:
        return 150.00
    
    def get_type(self) -> str:
        return "Consulta de Rotina"

#consulta de emergência
class EmergencyAppointment(Appointment):
    def __init__(self, pet: Pet, veterinarian: Veterinarian, date: str):
        super().__init__(pet, veterinarian, date)
    
    def get_price(self) -> float:
        return 300.00
    
    def get_type(self) -> str:
        return "Consulta de Emergência"

#consulta de vacinação
class VaccinationAppointment(Appointment):
    def __init__(self, pet: Pet, veterinarian: Veterinarian, date: str):
        super().__init__(pet, veterinarian, date)
    
    def get_price(self) -> float:
        return 80.00
    
    def get_type(self) -> str:
        return "Vacinação"

#factory - fábrica de consultas
class AppointmentFactory:
    @staticmethod
    def create_appointment(appointment_type: str, pet: Pet, 
                          veterinarian: Veterinarian, date: str) -> Appointment:
        if appointment_type == "routine":
            return RoutineAppointment(pet, veterinarian, date)
        elif appointment_type == "emergency":
            return EmergencyAppointment(pet, veterinarian, date)
        elif appointment_type == "vaccination":
            return VaccinationAppointment(pet, veterinarian, date)
        else:
            #retorna consulta de rotina como padrão
            return RoutineAppointment(pet, veterinarian, date)

#protocolo de notificação (interface)
class NotificationProtocol(Protocol):
    def appointment_updated(self, appointment: Appointment, action: str) -> None:
        ...

#gerenciador de consultas 
class AppointmentManager:
    def __init__(self):
        self._observers: list[NotificationProtocol] = []
        self._appointments: list[Appointment] = []
    
    def add_observer(self, observer: NotificationProtocol):
        self._observers.append(observer)
    
    def remove_observer(self, observer: NotificationProtocol):
        self._observers.remove(observer)
    
    def notify_all(self, appointment: Appointment, action: str):
        for observer in self._observers:
            observer.appointment_updated(appointment, action)
    
    def schedule_appointment(self, appointment: Appointment):
        self._appointments.append(appointment)
        self.notify_all(appointment, "agendada")
    
    def cancel_appointment(self, appointment: Appointment):
        appointment.status = "Cancelada"
        self.notify_all(appointment, "cancelada")
    
    def confirm_appointment(self, appointment: Appointment):
        appointment.status = "Confirmada"
        self.notify_all(appointment, "confirmada")

#notificação por email
class EmailNotification:
    def appointment_updated(self, appointment: Appointment, action: str):
        print(f"Email enviado para {appointment.pet.owner.email}")
        print(f"   Assunto: Consulta {action}")
        print(f"   Mensagem: Olá {appointment.pet.owner.name}!")
        print(f"   Sua consulta para {appointment.pet.name} foi {action}.")
        print(f"   Tipo: {appointment.get_type()}")
        print(f"   Data: {appointment.date}")
        print(f"   Veterinário: {appointment.veterinarian.name}")
        print(f"   Valor: R$ {appointment.get_price():.2f}\n")

#notificação por SMS
class SMSNotification:
    def appointment_updated(self, appointment: Appointment, action: str):
        print(f"SMS enviado para {appointment.pet.owner.phone}")
        print(f"   {appointment.pet.owner.name}, sua consulta para {appointment.pet.name}")
        print(f"   foi {action} em {appointment.date}.")
        print(f"   Veterinário: Dr. {appointment.veterinarian.name.split()[-1]}")
        print(f"   Valor: R$ {appointment.get_price():.2f}\n")
    
#função principal
def main():    
    print("Sistema de Agendamento Veterinário\n")
    
    #ciando clientes
    client1 = Client(
        name = "Isabella",
        email = "isa@gmail.com",
        id = "123456",
        phone = "(63)91234-1234"
    )
    
    client2 = Client(
        name = "Thiago",
        email = "tato@gmail.com",
        id = "789101",
        phone = "(63)99999-8888"
    )
    
    #criando pets
    pet1 = Pet(
        name = "Peppa",
        species = "Cachorro",
        age = 5,
        owner = client1
    )
    
    pet2 = Pet(
        name = "Pituchinha",
        species = "Gato",
        age = 3,
        owner = client2
    )

    vet1 = Veterinarian(
        name = "Dr. Lino Moraes",
        email = "lino@vetclinica.com",
        id = "CRMV-12345",
        phone = "(63)98888-7777",
        specialty = "Clínica Geral"
    )
    
    #testando
    print(client1)
    print(f"Pet: {pet1}\n")
    
    print(client2)
    print(f"Pet: {pet2}\n")

    print("\nVeterinário:")
    print(vet1)
    print()
    
#testando o factory e observer pattern
    print("Agendamento com Notificações\n")
    
    #criando o gerenciador de consultas
    manager = AppointmentManager()
    
    #criando os observadores (notificações)
    email_notification = EmailNotification()
    sms_notification = SMSNotification()
    
    #registrando os observadores no gerenciador
    manager.add_observer(email_notification)
    manager.add_observer(sms_notification)
    
    #criando diferentes tipos de consultas usando a factory
    appointment1 = AppointmentFactory.create_appointment(
        appointment_type = "routine",
        pet = pet1,
        veterinarian = vet1,
        date = "20/11/2025"
    )
    
    appointment2 = AppointmentFactory.create_appointment(
        appointment_type = "emergency",
        pet = pet2,
        veterinarian = vet1,
        date = "18/11/2025"
    )
    
    appointment3 = AppointmentFactory.create_appointment(
        appointment_type = "vaccination",
        pet = pet1,
        veterinarian = vet1,
        date = "22/11/2025"
    )
    
    #agendando consultas
    print("Agendando consultas...")
    manager.schedule_appointment(appointment1)
    manager.schedule_appointment(appointment2)
    manager.schedule_appointment(appointment3)
    
    #exibindo as consultas criadas
    print(f"\n{appointment1}")
    print(appointment2)
    print(appointment3)
    print()

#testando cancelamento e confirmação
    print("\nTestando\n")
    
    print("Confirmando consulta de rotina...")
    manager.confirm_appointment(appointment1)
    
    print("\nCancelando consulta de emergência...")
    manager.cancel_appointment(appointment2)

if __name__ == "__main__":
    main()