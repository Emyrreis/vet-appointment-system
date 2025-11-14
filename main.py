#classe do cliente
class Client:
    def __init__(self, name: str, email: str, id: str, phone: str):
        self.__name = name
        self.__email = email
        self.__id = id
        self.__phone = phone
    
    #getters - acesso aos atributos privados
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def id(self) -> str:
        return self.__id
    
    @property
    def phone(self) -> str:
        return self.__phone
    
    #setters - modificar os atributos privados
    @email.setter
    def email(self, new_email: str):
        self.__email = new_email
    
    @phone.setter
    def phone(self, new_phone: str):
        self.__phone = new_phone
    
    def __str__(self) -> str:
        return f"Cliente: {self.__name} | Email: {self.__email} | Telefone: {self.__phone}"

#classe do pet
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
    print("Sistema de Agendamento Veterinário: \n")
    
    #criando clientes
    client1 = Client(
        name = "Thiago",
        email = "tatato@email.com",
        id = "123456",
        phone = "(63)98765-4321"
    )
    
    client2 = Client(
        name = "Isabella",
        email = "isa@email.com",
        id = "654321",
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
    
    #testando os dados
    print(client1)
    print(f"Pet: {pet1}\n")
    
    print(client2)
    print(f"Pet: {pet2}\n")


if __name__ == "__main__":
    main()