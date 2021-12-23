def help_print():
    """
    Отображает информацию о командах
    :return:
    """
    print("Command - 'loc' - заращивает почтовы индекс, возвращает город и штат \n"
          "Command - 'zip' - запрашивает город и штат, возвращает почтовый индекс \n,"
          "Command - 'dist' - определяет расстояние между двумя почтовыми станциями \n,"
          "Command - 'help' - информация о командах \n,"
          "Command - 'end' - завершение приложение \n")




def main():
    # logging.basicConfig(level=logging.DEBUG)
    rfh = logging.handlers.RotatingFileHandler(
        filename='zip_app.log',
        mode='a',
        maxBytes=5*1024*1024,
        backupCount=9,
        encoding=None,
        delay=0
    )
    logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
                        handlers=[rfh])
    logger = logging.getLogger('main')

    zip_codes = util.read_zip_all()

    command = ""
    while command != 'end':
        command = input("Command ('loc', 'zip', 'dist', 'help', 'end') => ")
        # logging.info(f'Received command {command}')
        logger.info(f'Received command {command}')
        print(command)
        command = command.strip().lower()
        if command == 'loc':
            process_loc(zip_codes)
        elif command == 'zip':
            process_zip(zip_codes)
        elif command == 'dist':
            process_dist(zip_codes)
        elif command == 'help':
            help_print()
        elif command != 'end':
            print("Invalid command, ignoring")
        print()
    print("Done")
    logging.shutdown()

if __name__ == "__main__":
    main()
