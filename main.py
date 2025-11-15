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
    
    #testando
    print(client1)
    print(f"Pet: {pet1}\n")
    
    print(client2)
    print(f"Pet: {pet2}\n")


if __name__ == "__main__":
    main()