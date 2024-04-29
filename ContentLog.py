import csv
import os.path
import pandas

def main():
    message = "1 Games, 2 Movies, 3 Shows, 0 Exit"
    print(message)
    menu = float(input("Choice: "))
    print()

    while menu != 0:
        if menu == 1:
            gameFunc()
        elif menu == 2:
            movieFunc()
        elif menu == 3:
            showFunc()

        print(message)
        menu = float(input("Choice: "))
        print()

def gameFunc(): 
    message = "1 Add, 2 Change, 3 Delete, 0 Exit"
    file = "game.csv"
    if os.path.isfile(file):
        if lineCount(file) == 1:
            game = addGameQuestion()
            addGame(file, game)
    else:
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)
            x = ("Game", "Console")
            writer.writerow(x)

        game = addGameQuestion()
        addGame(file, game)

    displayGame(file)

    print(message)
    menu = float(input("Choice: "))
    print()

    while menu != 0:
        if menu == 1:
            game = addGameQuestion()
            addGame(file, game)
        elif menu == 2:
            changeGame(file)
        elif menu == 3:
            num = float(input("Game # to be deleted: "))

            deleteGame(file, num)

        displayGame(file)

        print(message)
        menu = float(input("Choice: "))
        print()

def movieFunc():
    message = "1 Add, 2 Change, 3 Delete, 0 Exit"
    file = "movie.csv"
    if os.path.isfile(file):
        if lineCount(file) == 1:
            movie = addMovieQuestion()
            addMovie(file, movie)
    else:
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)
            x = ("Movie", "Genre")
            writer.writerow(x)

        movie = addMovieQuestion()
        addMovie(file, movie)

    displayMovie(file)

    print(message)
    menu = float(input("Choice: "))
    print()

    while menu != 0:
        if menu == 1:
            movie = addMovieQuestion()
            addMovie(file, movie)
        elif menu == 2:
            changeMovie(file)
        elif menu == 3:
            num = float(input("Movie # to be deleted: "))

            deleteMovie(file, num)

        displayMovie(file)

        print(message)
        menu = float(input("Choice: "))
        print()

def showFunc():
    message = "1 Add, 2 Change, 3 Delete, 0 Exit"
    file = "show.csv"
    if os.path.isfile(file):
        if lineCount(file) == 1:
            show = addShowQuestion()
            addShow(file, show)
    else:
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)
            x = ("Show", "Season", "Episode", "Finished")
            writer.writerow(x)

        show = addShowQuestion()
        addShow(file, show)

    displayShow(file)

    print(message)
    menu = float(input("Choice: "))
    print()

    while menu != 0:
        if menu == 1:
            show = addShowQuestion()
            addShow(file, show)
        elif menu == 2:
            changeShow(file)
        elif menu == 3:
            num = float(input("Show # to be deleted: "))

            deleteShow(file, num)

        displayShow(file)

        print(message)
        menu = float(input("Choice: "))
        print()

def displayGame(file):
    with open(file, "r") as fr:
        reader = csv.reader(fr)

        count = 0

        for line in reader:
            if count == 0:
                print("# - Name - Console")
                count += 1
                continue
            line = ','.join(line)
            line = line.replace(",", " - ")
            print(str(count) + " - " + line)
            count += 1
        print()

def displayMovie(file):
    with open(file, "r") as fr:
        reader = csv.reader(fr)

        count = 0

        for line in reader:
            if count == 0:
                print("# - Name - Genre")
                count += 1
                continue
            line = ','.join(line)
            line = line.replace(",", " - ")
            print(str(count) + " - " + line)
            count += 1
        print()

def displayShow(file):
    with open(file, "r") as fr:
        reader = csv.reader(fr)

        count = 0

        for line in reader:
            if count == 0:
                print("# - Name - Season - Episode - Finished")
                count += 1
                continue

            season = line[1]
            episode = line[2]
            finished = line[3]
            
            line[1] = f"S{season}"
            line[2] = f"E{episode}"
            if finished == "y":
                line[3] = "Yes"
            else:
                line[3] = "No"

            line = ','.join(line)
            line = line.replace(",", " - ")
            print(str(count) + " - " + line)
            count += 1
        print()

def addGameQuestion():
    gameName = input("Game Name: ")
    gameConsole = input("Game Console: ")
    print()
    game = (gameName + "," + gameConsole + "\n")
    return game

def addMovieQuestion():
    movieName = input("Movie Name: ")
    movieGenre = input("Movie Genre: ")
    print()
    movie = (movieName + "," + movieGenre + "\n")
    return movie

def addShowQuestion():
    showName = input("Show Name: ")
    showSeason = input("Show Season: ")
    showEpisode = input("Show Episode: ")
    showFinished = input("Show finished (y/n): ")
    if showFinished != "y":
        showFinished == "n"
    print()
    show = (showName + "," + showSeason + "," + showEpisode + "," + showFinished + "\n")
    return show

def addGame(file, game):
    with open(file, "a") as fa:
        fa.write(game)
    sortGame(file)

def addMovie(file, movie):
    with open(file, "a") as fa:
        fa.write(movie)
    sortMovie(file)

def addShow(file, show):
    with open(file, "a") as fa:
        fa.write(show)
    sortShow(file)

def changeGame(file):
    num = float(input("Game # to be changed: "))
    conf = ""
    tempFile = "tempGame.csv"

    oldGameName = ""
    oldGameConsole = ""
    newGameName = ""
    newGameConsole = ""

    if num != 0:
        if num > 0 and num < lineCount(file):
            
            with open(file, "r") as fr:
                reader = csv.reader(fr)
                
                count = 0

                for line in reader:
                    if count != num:
                        count += 1
                        continue
                    oldGameName = line[0]
                    oldGameConsole = line[1]
                    line = ",".join(line)
                    line = line.replace(",", " - ")
                    print(f"Do you want to change this: {line}")
                    conf = input("Choice (y/n): ")
                    print()
                    break

            if conf == "y":

                newGameName = input("New name: ")
                if newGameName == "":
                    newGameName = oldGameName

                newGameConsole = input("New console: ")
                if newGameConsole == "":
                    newGameConsole = oldGameConsole
                
                if newGameName != oldGameName or newGameConsole != oldGameConsole:

                    with open(file, "r") as fr:

                        reader = csv.reader(fr)

                        count = 0

                        with open(tempFile, "w", newline="") as fw:
                            writer = csv.writer(fw)

                            x = 0

                            for line in reader:

                                if x == num:
                                    x += 1
                                    continue
                                writer.writerow(line)
                                x += 1

                    if os.path.isfile(file) and conf == "y":
                        os.remove(file)
                        os.rename(tempFile, file)
                        game = (newGameName + "," + newGameConsole + "\n")
                        addGame(file, game)
                    else:
                        print()
                
    else:
        print()   

def changeMovie(file):
    num = float(input("Movie # to be changed: "))
    conf = ""
    tempFile = "tempMovie.csv"

    oldMovieName = ""
    oldMovieGenre = ""
    newMovieName = ""
    newMovieGenre = ""

    if num != 0:
        if num > 0 and num < lineCount(file):
            
            with open(file, "r") as fr:
                reader = csv.reader(fr)
                
                count = 0

                for line in reader:
                    if count != num:
                        count += 1
                        continue
                    oldMovieName = line[0]
                    oldMovieGenre = line[1]
                    line = ",".join(line)
                    line = line.replace(",", " - ")
                    print(f"Do you want to change this: {line}")
                    conf = input("Choice (y/n): ")
                    print()
                    break

            if conf == "y":

                newMovieName = input("New name: ")
                if newMovieName == "":
                    newMovieName = oldMovieName

                newMovieGenre = input("New Genre: ")
                if newMovieGenre == "":
                    newMovieGenre = oldMovieGenre
                
                if newMovieName != oldMovieName or newMovieGenre != oldMovieGenre:

                    with open(file, "r") as fr:

                        reader = csv.reader(fr)

                        count = 0

                        with open(tempFile, "w", newline="") as fw:
                            writer = csv.writer(fw)

                            x = 0

                            for line in reader:

                                if x == num:
                                    x += 1
                                    continue
                                writer.writerow(line)
                                x += 1

                    if os.path.isfile(file) and conf == "y":
                        os.remove(file)
                        os.rename(tempFile, file)
                        movie = (newMovieName + "," + newMovieGenre + "\n")
                        addMovie(file, movie)
                    else:
                        print()
                
    else:
        print()  

def changeShow(file):
    num = float(input("Show # to be changed: "))
    conf = ""
    tempFile = "tempShow.csv"

    oldShowName = ""
    oldShowSeason = ""
    oldShowEpisode = ""
    oldShowFinished = ""
    newShowName = ""
    newShowSeason = ""
    newShowEpisode = ""
    newShowFinished = ""

    if num != 0:
        if num > 0 and num < lineCount(file):
            
            with open(file, "r") as fr:
                reader = csv.reader(fr)
                
                count = 0

                for line in reader:
                    if count != num:
                        count += 1
                        continue
                    oldShowName = line[0]
                    oldShowSeason = line[1]
                    oldShowEpisode = line[2]
                    oldShowFinished = line[3]

                    season = line[1]
                    episode = line[2]
                    finished = line[3]
                    
                    line[1] = f"S{season}"
                    line[2] = f"E{episode}"
                    if finished == "y":
                        line[3] = "Yes"
                    else:
                        line[3] = "No"

                    line = ",".join(line)
                    line = line.replace(",", " - ")
                    print(f"Do you want to change this: {line}")
                    conf = input("Choice (y/n): ")
                    print()
                    break

            if conf == "y":

                newShowName = input("New name: ")
                if newShowName == "":
                    newShowName = oldShowName

                newShowSeason = input("New season: ")
                if newShowSeason == "":
                    newShowSeason = oldShowSeason

                newShowEpisode = input("New episode: ")
                if newShowEpisode == "":
                    newShowEpisode = oldShowEpisode

                newShowFinished = input("New finished (y/n): ")
                if newShowFinished != "y":
                    newShowFinished == ""
                if newShowFinished == "":
                    newShowFinished = oldShowFinished
                
                if newShowName != oldShowName or newShowSeason != oldShowSeason or newShowEpisode != oldShowEpisode or newShowFinished != oldShowFinished:

                    with open(file, "r") as fr:

                        reader = csv.reader(fr)

                        count = 0

                        with open(tempFile, "w", newline="") as fw:
                            writer = csv.writer(fw)

                            x = 0

                            for line in reader:

                                if x == num:
                                    x += 1
                                    continue
                                writer.writerow(line)
                                x += 1

                    if os.path.isfile(file) and conf == "y":
                        os.remove(file)
                        os.rename(tempFile, file)
                        show = (newShowName + "," + newShowSeason + "," + newShowEpisode + "," + newShowFinished + "\n")
                        addShow(file, show)
                    else:
                        print()
                
    else:
        print() 

def deleteGame(file, num):
    conf = "n"
    if num != 0:
        if num > 0 and num < lineCount(file):
            tempFile = "tempGame.csv"

            with open(file, "r") as fr:
                    reader = csv.reader(fr)

                    count = 0

                    for line in reader:
                        if count != num:
                            count += 1
                            continue
                        line = ','.join(line)
                        line = line.replace(",", " - ")
                        print(f"Do you want to delete this: {line}")
                        conf = input("Choice (y/n): ")
                        print()
                        break

            with open(file, "r") as fr:

                reader = csv.reader(fr)

                count = 0

                if conf == "y":

                    with open(tempFile, "w", newline="") as fw:
                        writer = csv.writer(fw)

                        x = 0

                        for line in reader:

                            if x == num:
                                x += 1
                                continue
                            writer.writerow(line)
                            x += 1

            if os.path.isfile(file) and conf == "y":
                os.remove(file)
                os.rename(tempFile, file)

        else:
            print()
            print("------------")
            print("Wrong Input!")
            print("------------")
            print()
    else:
        print()

def deleteMovie(file, num):
    conf = "n"
    if num != 0:
        if num > 0 and num < lineCount(file):
            tempFile = "tempMovie.csv"

            with open(file, "r") as fr:
                    reader = csv.reader(fr)

                    count = 0

                    for line in reader:
                        if count != num:
                            count += 1
                            continue
                        line = ','.join(line)
                        line = line.replace(",", " - ")
                        print(f"Do you want to delete this: {line}")
                        conf = input("Choice (y/n): ")
                        print()
                        break

            with open(file, "r") as fr:

                reader = csv.reader(fr)

                count = 0

                if conf == "y":

                    with open(tempFile, "w", newline="") as fw:
                        writer = csv.writer(fw)

                        x = 0

                        for line in reader:

                            if x == num:
                                x += 1
                                continue
                            writer.writerow(line)
                            x += 1

            if os.path.isfile(file) and conf == "y":
                os.remove(file)
                os.rename(tempFile, file)

        else:
            print()
            print("------------")
            print("Wrong Input!")
            print("------------")
            print()
    else:
        print()

def deleteShow(file, num):
    conf = "n"
    if num != 0:
        if num > 0 and num < lineCount(file):
            tempFile = "tempShow.csv"

            with open(file, "r") as fr:
                    reader = csv.reader(fr)

                    count = 0

                    for line in reader:
                        if count != num:
                            count += 1
                            continue
                        line = ','.join(line)
                        line = line.replace(",", " - ")
                        print(f"Do you want to delete this: {line}")
                        conf = input("Choice (y/n): ")
                        print()
                        break

            with open(file, "r") as fr:

                reader = csv.reader(fr)

                count = 0

                if conf == "y":

                    with open(tempFile, "w", newline="") as fw:
                        writer = csv.writer(fw)

                        x = 0

                        for line in reader:

                            if x == num:
                                x += 1
                                continue
                            writer.writerow(line)
                            x += 1

            if os.path.isfile(file) and conf == "y":
                os.remove(file)
                os.rename(tempFile, file)

        else:
            print()
            print("------------")
            print("Wrong Input!")
            print("------------")
            print()
    else:
        print()
   
def sortGame(file):
    csv_file = pandas.read_csv(file)
    sort = csv_file.sort_values(by=["Game"])
    sort.to_csv(file, index=False)

def sortMovie(file):
    csv_file = pandas.read_csv(file)
    sort = csv_file.sort_values(by=["Movie"])
    sort.to_csv(file, index=False)

def sortShow(file):
    csv_file = pandas.read_csv(file)
    sort = csv_file.sort_values(by=["Show"])
    sort.to_csv(file, index=False)

def lineCount(file):
    line_count = 0
    with open(file, "r") as fr:

        for line in fr:
            if line.strip():
                line_count += 1

    return line_count

main()