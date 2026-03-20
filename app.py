import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from playsound import playsound

from utils.audio_recorder import gravar_audio


def carregar_cliente() -> OpenAI:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "Defina OPENAI_API_KEY no arquivo .env antes de executar o projeto."
        )
    return OpenAI(api_key=api_key)


BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "audio"
INPUT_AUDIO = AUDIO_DIR / "input.wav"
OUTPUT_AUDIO = AUDIO_DIR / "resposta.mp3"


SYSTEM_PROMPT = (
    "Você é um assistente de voz útil e objetivo. "
    "Responda sempre em português do Brasil, de forma natural e clara."
)


client = carregar_cliente()


def transcrever_audio(caminho_audio: Path) -> str:
    with open(caminho_audio, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )
    return transcript.text.strip()



def gerar_resposta(texto_usuario: str) -> str:
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": texto_usuario},
        ],
    )
    return resposta.choices[0].message.content.strip()



def gerar_audio(texto: str, caminho_saida: Path) -> None:
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=texto,
    ) as response:
        response.stream_to_file(str(caminho_saida))



def tocar_audio(caminho_audio: Path) -> None:
    playsound(str(caminho_audio))



def garantir_pastas() -> None:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)



def escolher_modo() -> str:
    print("\nEscolha uma opção:")
    print("1. Usar um arquivo de áudio já existente")
    print("2. Gravar um novo áudio pelo microfone")
    return input("Digite 1 ou 2: ").strip()



def processar_fluxo() -> None:
    texto_usuario = transcrever_audio(INPUT_AUDIO)
    print(f"\nVocê disse:\n{texto_usuario}")

    resposta = gerar_resposta(texto_usuario)
    print(f"\nAssistente:\n{resposta}")

    gerar_audio(resposta, OUTPUT_AUDIO)
    print(f"\nÁudio gerado em: {OUTPUT_AUDIO}")

    tocar = input("\nDeseja reproduzir o áudio agora? (s/n): ").strip().lower()
    if tocar == "s":
        tocar_audio(OUTPUT_AUDIO)



def main() -> None:
    garantir_pastas()

    print("=" * 50)
    print("Chat por Voz com OpenAI")
    print("=" * 50)

    try:
        modo = escolher_modo()

        if modo == "2":
            duracao_str = input("Quantos segundos deseja gravar? ").strip()
            duracao = int(duracao_str) if duracao_str.isdigit() else 5
            gravar_audio(nome_arquivo=str(INPUT_AUDIO), duracao=duracao)
        elif modo != "1":
            print("Opção inválida.")
            return

        if not INPUT_AUDIO.exists():
            print(f"Arquivo não encontrado em: {INPUT_AUDIO}")
            print("Coloque um arquivo WAV nessa pasta ou escolha a opção de gravação.")
            return

        processar_fluxo()

    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")
    except Exception as erro:
        print(f"\nErro durante a execução: {erro}")


if __name__ == "__main__":
    main()
