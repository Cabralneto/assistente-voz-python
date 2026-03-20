# Chat por Voz com OpenAI

Projeto em Python que:
- recebe um áudio do usuário
- transcreve o áudio em texto
- gera uma resposta com IA
- converte a resposta em voz
- reproduz o áudio final

## Tecnologias
- Python
- OpenAI API
- Speech to Text
- Responses API
- Text to Speech

## Estrutura do projeto

```text
voz-chatgpt/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── audio/
│   └── .gitkeep
└── utils/
    └── audio_recorder.py
```

## Como executar

### 1) Clone o repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd voz-chatgpt
```

### 2) Crie e ative um ambiente virtual

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3) Instale as dependências

```bash
pip install -r requirements.txt
```

### 4) Configure a chave da API

Crie um arquivo `.env` na raiz do projeto e adicione:

```env
OPENAI_API_KEY=sua_chave_aqui
```

### 5) Rode o projeto

```bash
python app.py
```

## Formas de usar

### Opção 1
Coloque um arquivo WAV em `audio/input.wav` e escolha a opção 1.

### Opção 2
Escolha a opção 2 para gravar o áudio direto pelo microfone.

## Fluxo do projeto

1. O usuário fornece um áudio.
2. O áudio é transcrito.
3. O texto é enviado para o modelo.
4. A resposta gerada é convertida em voz.
5. O sistema salva o resultado em `audio/resposta.mp3`.

## Melhorias que você pode fazer depois
- interface com Streamlit ou Gradio
- histórico de conversas
- escolha de vozes
- escolha de idioma
- gravação contínua
- deploy

## Observação
As vozes e os modelos podem ser alterados facilmente no arquivo `app.py`.
