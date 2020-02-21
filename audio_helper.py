from pydub import AudioSegment
import config

def create_sound(suffix, prefix="sounds/ns_prefix.wav"):

    prefix_sound = AudioSegment.from_file(prefix)
    suffix_sound = AudioSegment.from_file(suffix)

    combined_sound = prefix_sound + suffix_sound

    return combined_sound

#combined.export("./output.mp3", format='mp3')