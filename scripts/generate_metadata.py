import os

def generate_metadata(audio_folder, transcript_folder, output_csv):
    """
    Generates metadata.csv by mapping audio chunks to their corresponding transcripts.
    """
    metadata = []

    # Process each chunked transcript
    for file_name in sorted(os.listdir(transcript_folder)):
        if file_name.endswith(".txt"):
            base_name = os.path.splitext(file_name)[0]  # Remove .txt extension
            audio_file = base_name + ".wav"  # Corresponding audio chunk

            audio_path = os.path.join(audio_folder, audio_file)
            transcript_path = os.path.join(transcript_folder, file_name)

            if os.path.exists(audio_path):
                with open(transcript_path, "r") as f:
                    text = f.read().strip()
                    metadata.append(f"{audio_file}|{text}")

    # Write metadata.csv
    with open(output_csv, "w") as f:
        for entry in metadata:
            f.write(entry + "\n")

    print(f"✅ Metadata saved to {output_csv}")

if __name__ == "__main__":
    audio_folder = "data/my_custom_voice/wavs"  # Folder containing audio chunks
    transcript_folder = "data/my_custom_voice/split_transcripts"  # Folder with split text
    output_csv = "data/my_custom_voice/metadata.csv"  # Final metadata file

    generate_metadata(audio_folder, transcript_folder, output_csv)