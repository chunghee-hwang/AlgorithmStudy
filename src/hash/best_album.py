# https://programmers.co.kr/learn/courses/30/lessons/42579
from functools import cmp_to_key


def getPlayCntInSameGenre(genre, musics):
    same_genres = list(filter(lambda music: music[1] == genre, musics))
    same_genre_play_cnt = 0
    for idx, genre, play in same_genres:
        same_genre_play_cnt += play
    return same_genre_play_cnt


def compare_same_genre_musics(music1, music2):
    idx1 = music1[0]
    idx2 = music2[0]
    play1 = music1[2]
    play2 = music2[2]
    if play1 != play2: return play2 - play1
    return idx1 - idx2


def solution(genres, plays):
    answer = []
    musics = list(zip(range(len(genres)), genres, plays))
    same_genre_musics = {}
    genre_set = []
    for music in musics:
        genre = music[1]
        if genre not in same_genre_musics:
            same_genre_musics[genre] = [music]
            genre_set.append(genre)
        else:
            same_genre_musics[genre].append(music)
    for k, v in same_genre_musics.items():
        v.sort(key=cmp_to_key(compare_same_genre_musics))
    genre_set.sort(key=lambda g: getPlayCntInSameGenre(g, musics), reverse=True)
    for genre in genre_set:
        answer.extend(list(zip(*same_genre_musics[genre]))[0][:2])
    return answer
