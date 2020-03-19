# https://programmers.co.kr/learn/courses/30/lessons/42579
from collections import Counter
from functools import cmp_to_key
musics = []
def getPlayCntInSameGenre(genre):
    sameGenres = list(filter(lambda music: music[1] == genre, musics))
    sameGenrePlayCnt = 0
    for idx, genre, play in sameGenres:
        sameGenrePlayCnt+=play
    return sameGenrePlayCnt
def compareSameGenreMusics(music1, music2):
    idx1 = music1[0]
    idx2 = music2[0]
    play1 = music1[2]
    play2 = music2[2]
    if play1 != play2: return play2 - play1
    return idx1 - idx2
def solution(genres, plays):
    answer = []
    global musics
    musics = list(zip(range(len(genres)),genres, plays))
    sameGenreMusics = {}
    genreSet = []
    for music in musics:
        genre = music[1]
        if genre not in sameGenreMusics: 
            sameGenreMusics[genre] = [music]
            genreSet.append(genre)
        else: sameGenreMusics[genre].append(music)
    for k,v in sameGenreMusics.items():
        v.sort(key=cmp_to_key(compareSameGenreMusics))
    genreSet.sort(key=getPlayCntInSameGenre, reverse=True)
    for genre in genreSet:
        answer.extend(list(zip(*sameGenreMusics[genre]))[0][:2])
    return answer