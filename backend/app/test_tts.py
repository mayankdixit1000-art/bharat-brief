from backend.app.tts_service import generate_long_speech

text = """
Namaste! Welcome to Bharat Brief.

Aaj ki taza khabron mein hum desh aur duniya ki
mahatvapurna ghatnaon ke baare mein jaanenge.

Government ne naye development projects ki
ghoshna ki hai. In projects ka uddeshya
desh ke infrastructure aur public services
ko behtar banana hai.

Bharat Brief par aapko latest news
alag-alag Indian languages mein sunne ko milegi.
"""

audio = generate_long_speech(
    text=text,
    language_code="hi-IN"
)

with open("test_audio.mp3", "wb") as f:
    f.write(audio)

print("Full article audio generated successfully!")