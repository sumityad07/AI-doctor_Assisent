from brain_of_the_llm import encode_image_to_base64 , anayze_image
from voice_of_the_patient import record_audio, transcribe_audio
from voice_of_the_doctor import text_to_speach  
import gradio as gr

from dotenv import load_dotenv
load_dotenv()

system_prompt = """Act like a real doctor for learning purposes. Based on this image, describe any medical concerns you notice and suggest possible remedies. Avoid using numbers, special characters, or saying you're an AI. Speak directly to the person, starting with something like “With what I see...”. Keep it brief—maximum two sentences, one paragraph, no markdown."
""" 

def process_inputs(audio_filepath, image_filepath):
    speech_to_texta_output = transcribe_audio(filepath=audio_filepath, model_name="whisper-large-v3")
    if len(speech_to_texta_output) > 1000:
        speech_to_texta_output = speech_to_texta_output[:1000] + "..."

    if image_filepath:
        doctor_response = anayze_image(
            image_base64=encode_image_to_base64(image_filepath),
            query=system_prompt + "\n" + speech_to_texta_output,
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )

    else:
        doctor_response = "No image provided for analysis."

    # Convert the doctor's response to speech
    
    voice_of_the_doctor_file = text_to_speach(doctor_response, outfile_save="voice_of_the_doctor.mp3")
    return voice_of_the_doctor_file, doctor_response, speech_to_texta_output
    pass    

    

#create the interface


iface = gr.Interface(
    fn=process_inputs,
    inputs=[
       gr.Microphone(type="filepath", label="Record your voice"),

        gr.Image(type="filepath", label="Upload an image "),
    ],
    outputs=[
        gr.Audio(label="Voice of the doctor"),
        gr.Textbox(label="Doctor's advice"),
        gr.Textbox(label="Transcribed text from your voice"),
    ],
    title="Doctor's Assistant",
    description="This application allows you to record your voice and upload an image. The AI will analyze the image and provide medical advice based on the voice input. The doctor's response will be converted to speech and played back to you.",
)
iface.launch(debug=True)
