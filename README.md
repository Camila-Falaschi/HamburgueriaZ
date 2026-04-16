# 🍔 HamburgueriaZ

Aplicativo Android de pedido de hambúrguer desenvolvido como projeto prático de **Desenvolvimento Mobile**.

---

## 📱 Sobre o Projeto

O **HamburgueriaZ** é um app simples e funcional que simula um sistema de pedidos de lanchonete. O cliente informa seu nome, escolhe os adicionais do hambúrguer, define a quantidade e envia o pedido diretamente por e-mail.

---

## ✨ Funcionalidades

- **Campo de nome** — identificação do cliente (obrigatório)
- **Adicionais** — seleção de:
  - Bacon (+R$ 2,00)
  - Queijo (+R$ 2,00)
  - Onion Rings (+R$ 3,00)
- **Contador de quantidade** — botões de + e − (sem valores negativos)
- **Resumo em tempo real** — footer atualizado dinamicamente com itens e total
- **Envio por e-mail** — ao confirmar o pedido, abre o cliente de e-mail com o resumo preenchido
- **Validações** — aviso ao tentar enviar sem nome ou sem quantidade

---

## 💰 Tabela de Preços

| Item          | Preço     |
|---------------|-----------|
| Hambúrguer    | R$ 20,00  |
| + Bacon       | R$ 2,00   |
| + Queijo      | R$ 2,00   |
| + Onion Rings | R$ 3,00   |

---

## 🛠️ Tecnologias Utilizadas

- **Java** — linguagem principal
- **Android SDK** — minSdk 24 / targetSdk 36
- **XML Layouts** — `FrameLayout`, `ScrollView`, `LinearLayout`
- **Material Design** — componentes visuais e estilos
- **Intent `ACTION_SENDTO`** — envio de pedido por e-mail

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/HamburgueriaZ.git
   ```
2. Abra o projeto no **Android Studio**
3. Aguarde o Gradle sincronizar
4. Conecte um dispositivo ou inicie um emulador (API 24+)
5. Clique em **Run ▶**

---

## 📁 Estrutura do Projeto

```
HamburgueriaZ/
├── app/
│   └── src/
│       └── main/
│           ├── java/com/example/hamburgueriaz/
│           │   └── MainActivity.java
│           ├── res/
│           │   ├── layout/
│           │   │   └── activity_main.xml
│           │   ├── values/
│           │   │   ├── strings.xml
│           │   │   ├── colors.xml
│           │   │   └── themes.xml
│           │   └── drawable/
│           └── AndroidManifest.xml
└── README.md
```

