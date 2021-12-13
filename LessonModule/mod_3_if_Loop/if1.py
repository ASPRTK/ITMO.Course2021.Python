def isQrty(x,y):
    if (x > 0 and y > 0):
        return "Первая четверть"
    else:
        if (x > 0 and y < 0):
            return "Четвертая четверть"
        else:
            if (y > 0):
                return "Вторая четверть"
            else:
                return "Третья четверть"


if __name__ == "__main__":
	x = 2
	y = 5    
	print(isQrty(x,y))

