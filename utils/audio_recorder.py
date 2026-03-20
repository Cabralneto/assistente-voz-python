from pathlib import Path

import sounddevice as sd
from scipy.io.wavfile import write



def gravar_audio(nome_arquivo: str = "audio/input.wav", duracao: int = 5, sample_rate: int = 44100) -> None:
    caminho = Path(nome_arquivo)
    caminho.parent.mkdir(parents=True, exist_ok=True)

    print(f"\nGravando por {duracao} segundos...")
    audio = sd.rec(
        int(duracao * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
    )
    sd.wait()
    write(str(caminho), sample_rate, audio)
    print(f"Áudio salvo em: {caminho}")
