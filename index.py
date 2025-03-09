import os
import yt_dlp
import subprocess

def baixar_musica(url, pasta_destino='musicas'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
            'no_warnings': True,
            'ignoreerrors': False,
            'no_color': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            print(f"Música '{video_title}' baixada com sucesso!")
    
    except Exception as e:
        print(f"Erro ao baixar música: {e}")

def baixar_playlist(playlist_url, pasta_destino='musicas'):
    try:
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(pasta_destino, '%(playlist_title)s - %(title)s.%(ext)s'),
            'no_warnings': True,
            'ignoreerrors': True,
            'no_color': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=True)
            playlist_title = info_dict.get('title', 'Playlist')
            print(f"Playlist '{playlist_title}' baixada com sucesso!")
    
    except Exception as e:
        print(f"Erro ao baixar playlist: {e}")

def main():
    print("Bem-vindo ao Baixador de Músicas do YouTube")
    print("1. Baixar música única")
    print("2. Baixar playlist")
    
    opcao = input("Escolha uma opção (1/2): ")
    
    if opcao == '1':
        url = input("Digite a URL do vídeo do YouTube: ")
        baixar_musica(url)
    elif opcao == '2':
        url = input("Digite a URL da playlist do YouTube: ")
        baixar_playlist(url)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()