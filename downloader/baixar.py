import yt_dlp as ytdlp

class Downloader:
    def __init__(self, caminho_destino):
        self.caminho_destino = caminho_destino
        self.ffmpeg_location = 'C:/ffmpeg/bin'  #Caso necessário mude o caminho do ffmpeg. Mesmo caminho ultilizado no path

    def baixar_video(self, url):
        ydl_opts = {
            'format': 'mp4', 
            'outtmpl': f'{self.caminho_destino}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4', 
            'ffmpeg_location': self.ffmpeg_location,
        }
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def baixar_audio(self, url):
        ydl_opts = {
            'format': 'bestaudio/best', 
            'outtmpl': f'{self.caminho_destino}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': self.ffmpeg_location,
        }
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
