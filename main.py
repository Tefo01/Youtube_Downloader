from pytube import YouTube

def Download(link):
    youtube=YouTube(link)
    youtube=youtube.streams.get_highest_resolution()
    try:
        youtube.download()
    except:
        print("there has been an error")
    print("this download is completed")

    link=input("put your youtube link here URL: ")
    Download(link)