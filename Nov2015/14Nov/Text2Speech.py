"""
tex2speech trials
"""
__Date__ = '11/14/2015'
import pyglet
from gtts import gTTS
blabla = ("Pooooooooooi ?")
tts = gTTS(text=blabla, lang='en')
tts.save("C://test.mp3")
song = pyglet.media.load('C:/test.mp3',streaming=False)
player = song.play()
player.eos_action=player.EOS_LOOP
pyglet.app.run()
def exit_callback(dt):
    pyglet.app.exit()

pyglet.clock.schedule_once(exit_callback , 30)