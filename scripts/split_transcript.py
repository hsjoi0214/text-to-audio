import os
import math

def split_transcript(transcript, num_chunks):
    """
    Splits a transcript into roughly equal parts.
    """
    words = transcript.split()  # Split transcript into words
    chunk_size = math.ceil(len(words) / num_chunks)  # Approximate size per chunk
    split_transcripts = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return split_transcripts

def process_transcripts(transcript_file, audio_folder, output_folder):
    """
    Splits transcripts based on the number of chunks per audio file.
    """
    with open(transcript_file, "r") as f:
        transcript_data = [line.strip().split("|") for line in f.readlines()]

    os.makedirs(output_folder, exist_ok=True)

    for file_name, transcript in transcript_data:
        base_name = os.path.splitext(file_name)[0]  # Remove .wav extension
        audio_path = os.path.join(audio_folder, base_name + "_chunk_0.wav")  # Check if chunks exist

        if os.path.exists(audio_path):
            # Count how many chunks exist for this file
            num_chunks = len([f for f in os.listdir(audio_folder) if f.startswith(base_name)])

            # Split the transcript into matching parts
            split_texts = split_transcript(transcript, num_chunks)

            # Save split transcripts into individual text files
            for i, text in enumerate(split_texts):
                with open(os.path.join(output_folder, f"{base_name}_chunk_{i}.txt"), "w") as txt_file:
                    txt_file.write(text)

            print(f"Processed transcript for {file_name}: {num_chunks} chunks created.")

if __name__ == "__main__":
    transcript_file = "data/transcripts/transcripts.txt"  # Full transcripts
    audio_folder = "data/my_custom_voice/wavs"  # Processed audio chunks
    output_folder = "data/my_custom_voice/split_transcripts"  # Output folder for split texts

    process_transcripts(transcript_file, audio_folder, output_folder)