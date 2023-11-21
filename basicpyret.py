from pytube import YouTube, Playlist

def download_video(wlink):
    YouTube(wlink).streams.get_highest_resolution().download('downloads/')

def download_playlist(plink):
    plist = Playlist(plink)
    for video in plist.videos:
        video.streams.get_highest_resolution().download('downloads/')

def main():
    menutype = input('1: video      2: playlist\n enter choice:')
    if menutype != '1' and menutype != '2':
        print('invalid input')
    if menutype == '1':
        wlink_in = input('video url:')
        download_video(wlink_in)
    elif menutype == '2':
        plist_in = input('playlist url:')
        download_playlist(plist_in)

if __name__ == '__main__':
    main()
