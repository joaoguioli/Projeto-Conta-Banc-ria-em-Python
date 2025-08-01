
# 🏦 Projeto: Conta Bancária em Python

Este projeto demonstra o funcionamento de um sistema bancário simples em Python, com uso de classes, encapsulamento, métodos de classe e propriedades com `@property`.

## 📄 Descrição

O código apresenta duas versões de uma classe de conta bancária:

1. **`ContaBancaria`**: Implementação tradicional com ativação via método de classe.
2. **`ContaBancariaPythonica`**: Abordagem mais "pythônica", utilizando `@property` para acessar atributos privados.

### Funcionalidades implementadas:

- Criação de contas com titular e saldo.
- Exibição de informações da conta.
- Ativação de conta via método de classe.
- Uso de propriedades para acessar atributos privados de forma segura.

## 🧠 Conceitos utilizados

- `__init__`: Método construtor.
- `__str__`: Representação personalizada da conta.
- `@classmethod`: Para ativar contas externamente.
- `@property`: Encapsulamento de atributos privados.
- Atributos com underscore (`_`) para indicar uso interno.

## 📌 Exemplo de uso

```python
conta1 = ContaBancaria("João", 1000)
print(conta1)  # Conta de João - Saldo: R$1000

conta3 = ContaBancaria("Carlos", 200)
print(conta3._ativo)  # False
ContaBancaria.ativar_conta(conta3)
print(conta3._ativo)  # True

