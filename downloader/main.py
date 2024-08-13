from baixar import Downloader
from utils import obter_pasta_downloads, print_colored
import sys
import yt_dlp as ytdlp

def mostrar_menu():
    print("\nEscolha o formato do download:")
    print("1. MP4 (Vídeo)")
    print("2. MP3 (Áudio)")
    print("3. Sair")

def validar_url(url):
    try:
        with ytdlp.YoutubeDL() as ydl:
            ydl.extract_info(url, download=False)
        return True
    except Exception as e:
        print(f"URL inválida ou erro ao acessar: {e}")
        return False

def main():
    caminho_destino = obter_pasta_downloads()
    print_colored("Youtube Downloader", "36")
    
    while True:
        url = input("Digite a URL do vídeo: ")
        
        while not validar_url(url):
            url = input("Digite uma URL válida do vídeo: ")
        
        mostrar_menu()
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '3':
            print("Saindo do programa...")
            sys.exit(0)
        
        if escolha not in ['1', '2']:
            print("Opção inválida. Tente novamente.")
            continue
        
        downloader = Downloader(caminho_destino)
        
        if escolha == '1':
            print(f"Baixando vídeo em MP4 para {caminho_destino}...")
            downloader.baixar_video(url)
        elif escolha == '2':
            print(f"Baixando áudio em MP3 para {caminho_destino}...")
            downloader.baixar_audio(url)
        
        print("Download concluído.")
        
        continuar = input("Deseja baixar outro arquivo? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saindo do programa...")
            sys.exit(0)

if __name__ == "__main__":
    main()
