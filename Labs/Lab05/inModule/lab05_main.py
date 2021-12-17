from Labs.Lab05.inModule.lab05_coreGames import corGames
from Labs.Lab05.inModule.lab05_inOut import result, inputPlaer


def main():
    igrok1, igrok2 = inputPlaer()
    countPlayer01, countPlayer02 = corGames(igrok1, igrok2, 5)
    print('Итог счета: (', igrok1, '/', igrok2, ') - ', countPlayer01, ':', countPlayer02, sep='')
    result(countPlayer01, countPlayer02, igrok1, igrok2,  'По итогу сражения одержал победу:')


main()