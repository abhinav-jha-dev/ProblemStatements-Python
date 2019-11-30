# required libraries
from urllib.request import urlopen
from shutil import copyfileobj
import scipy.io.wavfile
import pydub

# Folder path to download audio
download_base = "D:\Projects\Github\Python Projects\ProblemStatements\Audio\downloads\source.mp3"

# mp3 file path
# mp3_filePath = "http://p.scdn.co/mp3-preview/35b4ce45af06203992a86fa729d17b1c1f93cac5"

# download file
# with urlopen(mp3_filePath) as in_stream, open(download_base+"source.mp3", 'wb') as out_file:
#     copyfileobj(in_stream, out_file)
# read mp3 file
mp3 = pydub.AudioSegment.from_mp3(download_base)
# convert to wav
mp3.export(download_base+"source.wav", format="wav")
# read wav file
rate, audData = scipy.io.wavfile.read(download_base+"source.wav")

print(rate)
print(audData)