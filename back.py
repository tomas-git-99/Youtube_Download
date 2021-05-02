import pytube
import http.client
import multiprocessing
import multiprocessing.managers
import shutil
import os
import subprocess
import platform


#destino=(r'D:\descarga')
#tmp_directory = os.path.join(os.getcwd(), 'tmp')
#destination=(r'D:\descarga\Python intermedio')


class Download_completo:

    def lista_calidad_mp4(self, st):
        link_youtube = st
        yt=pytube.YouTube(link_youtube)
        streams=yt.streams.filter(subtype="mp4").filter(adaptive=True).filter(type='video')
        calidad=[]
        for i in streams:
            if i.resolution:
                calidad.append(int(i.resolution[:-1]))

        calidad=list(set(calidad))
        calidad.sort(reverse=True)
        calidad=[str(x)+'p' for x in calidad]

        return calidad

    def lista_calidad_webm(self, s):
        yt = pytube.YouTube(s)
        descarga = yt.streams.filter(subtype="webm").filter(type="video")
        listado = []
        for i in descarga:
            if i.resolution:
                listado.append(int(i.resolution[:-1]))

        listado = list(set(listado))
        listado.sort(reverse=True)
        listado=[str(x)+'p' for x in listado]
        return listado

    def audio(self, st, save_2):
        self.save()
        self.destination = (save_2)
        yt = pytube.YouTube(st)
        download_audio = yt.streams.filter(type="audio").filter(adaptive=True).filter(subtype="mp4")[-1]
        self.titulo = yt.title
        self.st={'audio':download_audio}
        download_audio.download(filename_prefix="audio-", output_path=self.tmp_directory)
        download_audio = os.path.join(self.tmp_directory, "audio-"+self.st['audio'].default_filename)

        output=self.st['audio'].default_filename

        self.covertidor_ffmpeg_audio(download_audio)

        src_shutil = '.mp3'

        dest_shutil = os.path.join(self.destination, self.st["audio"].title+".mp3")
        os.remove(download_audio)
        shutil.move(src_shutil, dest_shutil)
        
    def covertidor_ffmpeg_audio(self, video):
        if platform.system()=='Windows':
            subprocess.call(['ffmpeg', '-i', video, '-vn', '.mp3']) #124k mp3
  

    def call_ffmpeg(self, video_stream, audio_stream, output_stream):
        if platform.system()=='Windows':
            subprocess.call(['ffmpeg', '-i', video_stream, '-i', audio_stream, '-c', 'copy', output_stream], creationflags = subprocess.CREATE_NO_WINDOW)
        else:
            subprocess.call(['ffmpeg', '-i', video_stream, '-i', audio_stream, '-c', 'copy', output_stream])


          
    def save(self):
        self.tmp_directory = os.path.join(os.getcwd(), 'tmp')
        #self.destination = (save_2)
        #os.makedirs(self.destination, exist_ok=True)
        os.makedirs(self.tmp_directory, exist_ok=True) 


    def download_intento(self, yt, res, type_codec, save_2):
        self.save()
        self.destination = (save_2)
        yt_2 = pytube.YouTube(yt)
        video_stream=yt_2.streams.filter(type="video").filter(adaptive=True).filter(subtype=type_codec).filter(resolution=res)[-1]
        audio_stream=yt_2.streams.filter(type="audio").filter(subtype=type_codec).order_by('abr')[-1]
    #full_download={'video':video_stream, 'audio':audio_stream}
    
        st={'video':video_stream, 'audio':audio_stream}

        video_stream.download(filename_prefix="video-", output_path=self.tmp_directory)
        audio_stream.download(filename_prefix="audio-", output_path=self.tmp_directory)
        video_stream = os.path.join(self.tmp_directory, "video-"+st['video'].default_filename)
        audio_stream = os.path.join(self.tmp_directory, "audio-"+st['audio'].default_filename)
        output_stream = st['video'].default_filename
        self.call_ffmpeg(video_stream, audio_stream, output_stream)
        os.remove(video_stream)
        os.remove(audio_stream)
        src_shutil = output_stream
        dest_shutil = os.path.join(self.destination, st['video'].default_filename)
        shutil.move(src_shutil, dest_shutil)
        


        

#casa = Download_completo()
#lista = casa.lista_calidad()

#print(lista)


