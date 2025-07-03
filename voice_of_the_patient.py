from dotenv import load_dotenv
load_dotenv()

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


logging.basicConfig(level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s')


def record_audio(filepath,timeout=20,phrase_time_limit=None):
    """

    Record audio from the microphone and save it to a file.
    
    :param filepath: Path to save the recorded audio file.
    :param timeout: Maximum time to wait for recording in seconds.
    :param phrase_time_limit: Maximum length of each phrase in seconds.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=14) as source:
            logging.info("urjusting the ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Recording audio...")

            #record the audio
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete. Saving audio to file...")
            #extract text from the audio
            wav_data=   audio.get_wav_data()
            audio_segmennt = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segmennt.export(filepath, format="mp3", bitrate="128k")

    except Exception as e:
        logging.error(f"An error occurred while recording audio: {e}")
        

from groq import Groq
stt_model="whisper-large-v3"

client = Groq()
def transcribe_audio(filepath, model_name):
    audio_file=open(filepath, "rb")
    transcribe = client.audio.transcriptions.create(
        model=model_name,
        language="en",
        file=audio_file
    )
    return transcribe.text


