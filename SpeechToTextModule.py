import whisper


def STT(file='question.mp3'):
    model = whisper.load_model("base")
    audio = whisper.load_audio(file)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")
    options = whisper.DecodingOptions(fp16=False)  # cpu一定要設置false
    result = whisper.decode(model, mel, options)
    return result.text