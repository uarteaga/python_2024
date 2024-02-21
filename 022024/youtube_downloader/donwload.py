from pytube import YouTube


url = "https://www.youtube.com/watch?v=sDj72zqZakE"

youtube = YouTube(url)

stream = youtube.streams.get_highest_resolution()

donwload_path = 'usr/local/bin/python3 /Users/ulisesartg/Desktop/Development'

stream.download()