import sys
import os
import shutil
import send2trash

# To store drives.
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

# To list the drives.
def listDirectories():
    listdir = os.listdir(os.getcwd())
    for drivers in listdir:
        print(drivers)

while True:
    print("1.Open \n2.Rename \n3.Move or Paste \n4.Copy or Paste \n5.Delete\n")
    result = input("\nChoose One: ")

    if result == '1':
        # System Quick Access.
        print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')
        print('Drives: ')

        for i in range(len(drives)):
            print(str(5 + i) + '. ' + drives[i])

        while True:
            inp = input("\nChoose One(For Drives Add the Name and add ':' at end): ")

            if inp == '1':
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '2':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '3':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '4':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break

            elif inp in drives:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct input / drive name.\n')

        while True:

            listDirectories()

            print('\n\n1. Exit the File Manager.')
            print('2. Go Back to Previous Directory.')
            res = input('\nChoose a file/folder: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    os.system('"' + res + '"')
                else:
                    os.chdir(res)

            elif res == '1':                          # Exit command to exit from loop
                sys.exit(0)

            elif res == '2':                          # Back command to go up one directory
                os.chdir('..')

            else:
                print('No file/folder exist of this name.')

    if result == '2':
        print("You chose to rename")
        print('Drives: ')

        for i in range(len(drives)):
            print(str(1 + i) + '. ' + drives[i])

        while True:
            inp = input("\nChoose One(For Drives Add the Name and add ':' at end): ")
            
            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirectories()

            print('\n\n1. Exit the File Manager.')
            print('2. Go Back to Previous.')
            print('3. Rename Directory.')

            res = input('\nChoose a file to rename: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):

                    new_name = input("Enter a new name: ")
                    ogDir = res
                    newDir = os.getcwd() + '\\' + new_name
                    shutil.move(ogDir, newDir)
                else:
                    os.chdir(res)

            elif res == '1':    # Exit command to exit from loop
                sys.exit(0)

            elif res == '2':    # Back command to go up one directory
                os.chdir('..')

            elif res == '3':  # Rename command to delete one directory
                new_name = input("Enter a new name: ")
                ogDir = os.getcwd()
                os.chdir('..')
                newDir = os.getcwd() + '\\' + new_name
                shutil.move(ogDir, newDir)

            else:
                print('No file/folder exist of this name.')

    if result == '3':
        print("You chose to move")
        print('Drives: ')
        for i in range(len(drives)):
            print(str(1 + i) + '. ' + drives[i])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirectories()

            print('\n\n1. Exit the File Manager.')
            print('2. Go Back to Previous Directory.')
            print('3. To Cut the Directory.')

            res = input('\nChoose a file to move: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("\nMove " + res + " to a desired location.")

                    while True:
                        for i in range(len(drives)):
                            print(str(1 + i) + '. ' + drives[i])

                        inp2 = input("\nEnter your Choice: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a correct drive name.\n')

                    while True:
                        listDirectories()

                        print('1. Paste the Directory')

                        res2 = input('\nChoose a file to move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")
                            else:
                                os.chdir(res2)

                        elif res2 == '1':
                            shutil.move(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == '1':                          # Exit command to exit from loop
                sys.exit(0)

            elif res == '2':                          # Back command to go up one directory
                os.chdir('..')

            elif res == '3':
                og_path = os.getcwd()

                print("Moving the current directory")
                while True:
                    for i in range(len(drives)):
                        print(str(1 + i) + '. ' + drives[i])

                    inp2 = input("\nEnter your Choice: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:
                    listDirectories()

                    print('\n1. Paste the Directory.')

                    res2 = input('\nChoose a folder to open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")
                        else:
                            os.chdir(res2)

                    elif res2 == '1':
                        shutil.move(og_path, os.getcwd())
                        break

            else:
                print('No file/folder exist of this name.')

    if result == '4':
        print("You chose to copy")
        print('Drives: ')
        for i in range(len(drives)):
            print(str(1 + i) + '. ' + drives[i])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirectories()

            print('\n\n1. Exit the manager.')
            print('2. Go Back by one directory.')
            print('3. Copy the directory')

            res = input('\nChoose a file to copy: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("Move " + res + " to a desired location.")

                    while True:
                        for i in range(len(drives)):
                            print(str(1 + i) + '. ' + drives[i])

                        inp2 = input("\nEnter your Choice: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a correct drive name.\n')

                    while True:
                        listDirectories()

                        print('1. Paste the Directory.')
                        res2 = input('\nChoose a file to move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")
                            else:
                                os.chdir(res2)

                        elif res2 == '1':
                            shutil.copy(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == '1':  # Exit command to exit from loop
                sys.exit(0)

            elif res == '2':  # Back command to go up one directory
                os.chdir('..')

            elif res == '3':
                og_path = os.getcwd()

                print("Copying the current directory")
                while True:
                    for i in range(len(drives)):
                        print(str(1 + i) + '. ' + drives[i])

                    inp2 = input("\nEnter your Choice: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:
                    listDirectories()

                    print('\n1. Paste the Directory.')
                    res2 = input('\nChoose a folder to open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")
                        else:
                            os.chdir(res2)

                    elif res2 == '1':
                        print(og_path)
                        folder_name = og_path.split('\\')[-1]
                        folder_directory = os.getcwd() + '\\' + folder_name
                        shutil.copytree(og_path, folder_directory)
                        break

            else:
                print('No file/folder exist of this name.')

    if result == '5':
        while True:

            # Options to delete files/folders to permanently or otherwise
            print('\n1. Permanently Delete \n2. Send to Recycle Bin')
            query = input('Would you like to permanently delete or send to Recycle Bin?: ')

            if query == '1':
                print('You chose to permanently delete files/folders.\n')
                print('Drives: ')
                for i in range(len(drives)):
                    print(str(1 + i) + '. ' + drives[i])

                while True:
                    inp = input("\nEnter your Choice: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirectories()

                    print('\n\n1. Exit the manager.')
                    print('2. Go Back by one directory.')
                    print('3. Delete the Directory Permanently.')

                    res = input('\nChoose a file to delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            # Warning to prevent unnecessary deletion
                            print('Are you sure you want to permanently delete this file? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                os.unlink(res)
                        else:
                            os.chdir(res)

                    elif res == '1':                      # Exit command to exit from loop
                        sys.exit(0)

                    elif res == '2':                      # Back command to go up one directory
                        os.chdir('..')

                    elif res == '3':                    # Delete command to delete one directory

                        # Warning to prevent unnecessary deletion
                        print('Are you sure you want to permanently delete this folder? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            shutil.rmtree(path)

                    else:
                        print('No file/folder exist of this name.')

            elif query == '2':
                print('You chose to temporarily delete files/folders.')
                print('Drives: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])

                while True:
                    inp = input("\nEnter your Choice: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirectories()

                    print('\n\n1. Exit the manager.')
                    print('2. Go Back by one directory.')
                    print('3. Send to Recycle Bin.')


                    res = input('\nChoose a file to delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            # Warning to prevent unnecessary deletion
                            print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                send2trash.send2trash(res)
                        else:
                            os.chdir(res)

                    elif res == '1':  # Exit command to exit from loop
                        sys.exit(0)

                    elif res == '2':  # Back command to go up one directory
                        os.chdir('..')

                    elif res == '3':  # Delete command to delete one directory

                        # Warning to prevent unnecessary deletion
                        print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            send2trash.send2trash(path)

                    else:
                        print('No file/folder exist of this name.')

        else:
            print('You chose wrong number')