import sys
from mido import Message, MetaMessage, MidiFile, MidiTrack

if len(sys.argv) != 3:
    sys.exit("usage: python parser.py input_file output_prefix")

mid_motion = MidiFile()
mid_temp = MidiFile()
mid_light = MidiFile()

track_motion = MidiTrack()
track_temp = MidiTrack()
track_light = MidiTrack()

mid_motion.tracks.append(track_motion)
mid_temp.tracks.append(track_temp)
mid_light.tracks.append(track_light)

track_motion.append(MetaMessage('track_name', name=sys.argv[2]+'motion', time=0))
track_temp.append(MetaMessage('track_name', name=sys.argv[2]+'temp', time=0))
track_light.append(MetaMessage('track_name', name=sys.argv[2]+'light', time=0))


#track.append(Message('control_change', channel=0, control=4, value=27, time=60))
#mid.save('new_song3.mid')

with open(sys.argv[1]) as file:
        file_contents=file.read()
        
lines=file_contents.split('\n')
n=0
for index, val in enumerate(lines):    
    if val != "":
        print("index: "+str(index)+", val:"+str(val))
        track_motion.append(Message('control_change', channel=0, control=4, value=int(val.split(';')[1]), time=60))
        track_motion.append(Message('control_change', channel=0, control=4, value=int(val.split(';')[1]), time=60))
        track_temp.append(Message('control_change', channel=0, control=4, value=int(val.split(';')[2]), time=60))
        track_temp.append(Message('control_change', channel=0, control=4, value=int(val.split(';')[2]), time=60))
        track_light.append(Message('control_change', channel=0, control=4, value=int(val.split(';')[3]), time=60))
        track_light.append(Message('control_change', channel=0, control=4, value=int(val.split(';')[3]), time=60))
    else:
        print("=======================\nempty: "+str(index)+"\n=======================")
    
mid_motion.save(sys.argv[2]+'_motion.mid')
mid_temp.save(sys.argv[2]+'_temp.mid')
mid_light.save(sys.argv[2]+'_light.mid')