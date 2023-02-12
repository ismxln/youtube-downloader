from pytube import YouTube

if __name__ == '__main__':
    
    links = [
        'https://www.youtube.com/shorts/klmBTGQUkbM', 'https://www.youtube.com/watch?v=hS5CfP8n_js'
    ]

    counter = 0
    for link in links:
        yt = YouTube(link)
        
        print(f'Link #{counter}: {link}')
        counter += 1
        
        print(f'Title: {yt.title}')
        print(f'Views: {yt.views}')
        print(f'Info: {yt.streams.get_highest_resolution()}\n')

        yd = yt.streams.get_highest_resolution()

        path = 'D:/downloads'
        yd.download(path)  # folder where uploaded videos will be stored
