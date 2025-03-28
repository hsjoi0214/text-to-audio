from TTS.api import TTS

# Initialize the TTS model with the specified model name
tts = TTS(model_name="tts_models/en/vctk/vits")

# Print available speakers to confirm they are loaded correctly
print("Available speakers:", tts.speakers)

# Specify the speaker name (as a string, such as "p233")
speaker_name = "p233"  # Replace with any speaker ID like 'p341' if desired

# Check if the specified speaker is available in the model's speaker list
if speaker_name in tts.speakers:
    # Use the speaker name directly in the `speaker` parameter
    tts.tts_to_file(
        text="Hello, this is a test.",  # Text you want to convert to audio
        file_path="output.wav",         # Output file path for the generated audio
        speaker=speaker_name            # Specify the speaker name here
    )
    print(f"Audio generated for speaker {speaker_name} and saved to 'output.wav'")
else:
    # If the speaker is not found, print an error message
    print(f"Speaker '{speaker_name}' not found in the available speakers list.")
    

