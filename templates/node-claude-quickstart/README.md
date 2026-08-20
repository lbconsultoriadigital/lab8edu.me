# Node.js Claude API Quickstart / Início Rápido com Claude API em Node.js

[English](#english) | [Português](#português)

---

<a name="english"></a>
## English

A clean, modern boilerplate to interact with Anthropic's Claude API using official Node.js SDK and streaming responses.

### Getting Started

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Configure your API key and model**:
   Copy `.env.example` to `.env`, add your API key, and use a model ID currently supported by your Anthropic account:
   ```bash
   cp .env.example .env
   ```
   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ANTHROPIC_MODEL=your_current_anthropic_model_id
   ```
   Never commit the `.env` file.

3. **Run the script**:
   ```bash
   npm start
   ```

---

<a name="português"></a>
## Português

Um boilerplate moderno e limpo para interagir com a API do Claude da Anthropic utilizando o SDK oficial para Node.js com suporte a respostas em streaming.

### Como Começar

1. **Instale as dependências**:
   ```bash
   npm install
   ```

2. **Configure sua chave de API e o modelo**:
   Copie `.env.example` para `.env`, adicione sua chave e use um ID de modelo atualmente aceito pela sua conta Anthropic:
   ```bash
   cp .env.example .env
   ```
   ```env
   ANTHROPIC_API_KEY=sua_chave_da_anthropic_aqui
   ANTHROPIC_MODEL=id_atual_do_modelo_anthropic
   ```
   Nunca faça commit do arquivo `.env`.

3. **Execute o script**:
   ```bash
   npm start
   ```
