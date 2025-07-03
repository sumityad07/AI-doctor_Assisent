from gtts import gTTS 
import subprocess
from dotenv import load_dotenv
load_dotenv()



def text_to_speach(file,outfile_save):
    language = 'en'
    tts = gTTS(
        text=file,
        lang=language,
        slow=False
    )
    tts.save(outfile_save)
    # Play the audio file
    subprocess.run(["ffplay", "-nodisp", "-autoexit", outfile_save], check=True)
    

