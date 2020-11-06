##############################
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
def sample_recognize(local_file_path):
client = speech_v1.SpeechClient()
language_code = "ja-JP" # 言語コードを設定
sample_rate_hertz = 16000 # 周波数を16000
# データのエンコード
encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
config = {
"language_code": language_code,
"sample_rate_hertz": sample_rate_hertz,
"encoding": encoding,
}
with io.open(local_file_path, "rb") as f:
content = f.read()
audio = {"content": content}
response = client.recognize(config, audio)
for result in response.results:
alternative = result.alternatives[0] # 最初の候補である効率が最も高い
print(u"Transcript: {}".format(alternative.transcript))
if __name__ == '__main__':
sample_recognize('record/201008_001.MP3') # 音声認識したいファイルのパスを指定
##############################