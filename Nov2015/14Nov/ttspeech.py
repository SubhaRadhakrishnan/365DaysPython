__Date__ = '11/14/2015'
"""
tex2speech trials
"""
import pyglet
song = pyglet.media.load('C:/test.mp3',streaming=False)
player = song.play()
player.eos_action=player.EOS_LOOP
pyglet.app.run()