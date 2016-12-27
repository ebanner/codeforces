if __name__ == '__main__':
    n, d = [int(num) for num in raw_input().split()]
    song_lengths = [int(num) for num in raw_input().split()]

    t = joke_time = 0 # joke time is the time for jokes
    for i, song_length in enumerate(song_lengths):
        t += song_length # sing a song

        if i < n-1:
            t += 10
            joke_time += 10
        else:
            joke_time += d-t

    if t > d:
        print -1
    else:
        print joke_time / 5
