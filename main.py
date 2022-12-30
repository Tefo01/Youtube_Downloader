from pytube import YouTube

link = input("put your youtube link here URL: ")


def download(asd):
    print("1")
    youtube = YouTube(asd)
    youtube = youtube.streams.get_highest_resolution()

    try:
        youtube.download()
    except:
        print("there has been an error")

    print("this download is completed")
    print("2")


download(link)
