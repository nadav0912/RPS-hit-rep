import gradio as gr
import groq
import io
import numpy as np
import soundfile as sf
import os
from dotenv import load_dotenv
import pyttsx3


#load the file with the api key
load_dotenv()

groq_api = os.getenv('GROQ_API_KEY')
if groq_api:
    print(f"groq_api Key exists and begins {groq_api[:8]}")
else:
    print("groq api Key not set")


#tts function
def talker(text: str):
    """
    Convert the input text to speech using pyttsx3 and play it.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#stt function
def transcribe_audio(audio, api_key):
    if audio is None:
        return ""
    
    client = groq.Client(api_key= groq_api)
    
    # Convert audio to the format expected by the model
    # The model supports mp3, mp4, mpeg, mpga, m4a, wav, and webm file types 
    audio_data = audio[1]  # Get the numpy array from the tuple
    buffer = io.BytesIO()
    sf.write(buffer, audio_data, audio[0], format='wav')
    buffer.seek(0)

    bytes_audio = io.BytesIO()
    np.save(bytes_audio, audio_data)
    bytes_audio.seek(0)

    try:
        # Use Distil-Whisper English powered by Groq for transcription
        completion = client.audio.transcriptions.create(
            model="distil-whisper-large-v3-en",
            file=("audio.wav", buffer),
            response_format="text"
        )
        return completion
    except Exception as e:
        return f"Error in transcription: {str(e)}"

    
def process_audio(audio, api_key):
    api_key=groq_api
    if not api_key:
        return "Please enter your Groq API key.", "API key is required."
    transcription = transcribe_audio(audio, api_key)
    response = generate_response(transcription, api_key)
    return transcription, response



def generate_response(transcription, api_key):
    if not transcription:
        return "No transcription available. Please try speaking again."
    
    client = groq.Client(api_key=groq_api)
    
    try:

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": transcription}
            ],
        )
        reply = talker(completion.choices[0].message.content)
        return reply
    except Exception as e:
        return f"Error in response generation: {str(e)}"






# Custom CSS for the Groq badge and color scheme (feel free to edit however you wish)
custom_css = """
.gradio-container {
    background-color: #f5f5f5;
}
.gr-button-primary {
    background-color: #f55036 !important;
    border-color: #f55036 !important;
}
.gr-button-secondary {
    color: #f55036 !important;
    border-color: #f55036 !important;
}
#groq-badge {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
}
"""

with gr.Blocks(theme=gr.themes.Default()) as demo:
    gr.Markdown("# 🎙️ Groq x Gradio Voice-Powered AI Assistant")
    
    with gr.Row():
        audio_input = gr.Audio(label="Speak!", type="numpy")
    
    with gr.Row():
        transcription_output = gr.Textbox(label="Transcription")
        response_output = gr.Textbox(label="AI Assistant Response")
    
    submit_button = gr.Button("Process", variant="primary")
    
    # Add the Groq badge
    gr.HTML("""
    <div id="groq-badge">
        <div style="color: #f55036; font-weight: bold;">POWERED BY GROQ</div>
    </div>
    """)
    
    submit_button.click(
        process_audio,
        inputs=[audio_input],
        outputs=[transcription_output, response_output]
    )
    
    gr.Markdown("""
    ## How to use this app:
    1. Enter your [Groq API Key](https://console.groq.com/keys) in the provided field.
    2. Click on the microphone icon and speak your message (or forever hold your peace)! You can also provide a supported audio file. Supported audio files include mp3, mp4, mpeg, mpga, m4a, wav, and webm file types.
    3. Click the "Process" button to transcribe your speech and generate a response from our AI assistant.
    4. The transcription and AI assistant response will appear in the respective text boxes.
    
    """)

demo.launch()