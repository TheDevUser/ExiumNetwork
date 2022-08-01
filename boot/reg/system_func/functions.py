import os
import requests


def ThrowError(ErrorMessage):

    print(f"\033[0m\033[31m{ErrorMessage}")


def Pkg(cmdinput):

    Parameters = cmdinput.split(" ")

    if len(Parameters) <= 1:
        ThrowError("\nCorrect Usage : $ app <use> <file> <filename>\n")
    else:

        if len(Parameters) < 4 or len(Parameters) > 5:

            if len(Parameters) <= 2:

                ThrowError("\nCorrect Usage : $ app <use> <file> <filename>\n")

            else:

                if Parameters[1].lower() == "-r":

                    Filename = Parameters[2]

                    Filename = os.path.join("user/home/apps", Filename)

                    if not Filename.endswith(".app"): Filename += ".app"

                    if len(Parameters) == 3:

                        if not os.path.exists(Filename):
                            ThrowError(f"\n'{Filename}' does not exist.\n")
                        else:

                            with open(Filename) as f:
                                contents = f.read()
                                try:
                                    exec(contents)
                                except Exception as e:
                                    ThrowError("This code isn't executable")

                    else:
                        ThrowError(
                            "\nCorrect Usage : $ app <use> <file> <filename>\n"
                        )

                elif Parameters[1].lower() == "-u":

                    Filename = Parameters[2]

                    Filename = os.path.join("user/home/apps", Filename)

                    if not Filename.endswith(".app"): Filename += ".app"

                    if not os.path.exists(Filename):
                        ThrowError(f"'{Filename}' doesn't exist nigga")
                    else:
                        os.remove(Filename)
                        print("\nOperation Success, app removed.\n")
                else:  # They didnt write run or uninstall
                    ThrowError(
                        "\nCorrect Usage : $ app <use> <file> <filename>\n")
        else:
            Install = Parameters[1]
            PastebinLink = Parameters[2]
            Filename = Parameters[3]

            Filename = os.path.join("user/home/apps", Filename)

            if not Filename.endswith(".app"): Filename += ".app"
            if Install.lower() == "-i":

                try:
                    Res = requests.get(PastebinLink)

                    RawText = Res.text

                    if not os.path.exists(Filename):

                        f = open(Filename, "w")
                        f.write(RawText)
                        f.close()

                        print("\nOperation Success, app installed.")

                    else:

                        ThrowError(f"\n'{Filename}' is already install.\n")

                except Exception as e:
                    ThrowError("\nInvalid download URL\n")
            else:
                ThrowError("\nCorrect Usage : $ app <use> <URL> <filename>\n")
