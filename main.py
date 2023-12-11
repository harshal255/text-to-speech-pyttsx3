import pyttsx3

# Get user input for text and file name
text = input("Enter your text that you want to convert into speech: ")
file_name = input("Enter the desired name for the output file (without extension): ")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty("voices")

# Print available voices for the user to choose
print("Available Voices:")
for i, voice in enumerate(voices):
    print(f"{i + 1}. {voice.name}")

# Ask the user to choose a voice
selected_voice_index = int(input("Enter the number corresponding to the desired voice: ")) - 1
selected_voice = voices[selected_voice_index].id

# Set the chosen voice
engine.setProperty("voice", selected_voice)

# Set properties (optional)
# You can adjust the rate and volume according to your preference
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1)  # Volume level (0.0 to 1.0)

# Save the speech to an audio file
file_path = f"{file_name}.mp3"
engine.save_to_file(text, file_path)
engine.runAndWait()

# Close the audio file
engine.stop()



print(f"Speech saved to {file_path}")

