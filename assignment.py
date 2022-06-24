import datetime

DNI_TYGODNIA_PL = {
    0: 'poniedziałek',
    1: 'wtorek',
    2: 'środę',
    3: 'czwartek',
    4: 'piątek',
    5: 'sobote',
    6: 'niedziele'
}

NAZWY_MIESIECY_PL = {
    1: ['stycznia', 31],
    2: ['lutego', 29],
    3: ['marca', 31],
    4: ['kwietnia', 30],
    5: ['maja', 31],
    6: ['czerwca', 30],
    7: ['lipca', 31],
    8: ['sierpnia', 31],
    9: ['września', 30],
    10: ['października', 31],
    11: ['listopada', 30],
    12: ['grudnia', 31]
}

CYFRY_DLA_TYGODNIE_PL = {
    1: 'jeden',
    2: 'dwa',
    3: 'trzy',
    4: 'cztery',
}


# start_time = datetime.datetime(2023, 12, 31, 14, 30)

# reference_time = datetime.datetime(2022, 12, 30, 18, 50)


def natural_language(start_time, reference_time=datetime.datetime.now()):
    difference_year = start_time.year - reference_time.year
    difference_month = start_time.month - reference_time.month
    difference_days = start_time.day - reference_time.day
    difference_hour = start_time.hour - reference_time.hour
    difference_min = start_time.minute - reference_time.minute

    if difference_year == 0:
        if -4 <= difference_month < -1:
            if difference_days == 0:
                return f"{CYFRY_DLA_TYGODNIE_PL[abs(difference_month)]} miesiące temu o {start_time.hour}:{start_time.minute}"

        if difference_month == -1:
            if difference_days == 0:
                return f"miesiąc temu o {start_time.hour}:{start_time.minute}"
            if difference_days != 0:
                return f"{start_time.day} w zeszłym miesiącu o {start_time.hour}:{start_time.minute}"

        if difference_month == 0:

            if -21 < difference_days < -14:
                return (
                    f"{start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} o {start_time.hour}:{start_time.minute}")

            if - 14 < difference_days < -7:
                return (
                    f"tydzień temu w {DNI_TYGODNIA_PL[start_time.weekday()]} o {start_time.hour}:{start_time.minute}")

            if - 7 < difference_days < -1:
                if start_time.weekday() in (0, 1, 3, 4):
                    return f"w zeszły {DNI_TYGODNIA_PL[start_time.weekday()]} o {start_time.hour}:{start_time.minute}"
                if start_time.weekday() in (2, 5, 6):
                    return f"w zeszłą {DNI_TYGODNIA_PL[start_time.weekday()]} o {start_time.hour}:{start_time.minute}"

            if difference_days / 7 == -1:
                return f"tydzień temu o {start_time.hour}:{start_time.minute}"

            if difference_days / 7 in (-2.0, -3.0, -4.0):
                return (
                    f"{CYFRY_DLA_TYGODNIE_PL[abs(difference_days / 7)]} tygonie temu o {start_time.hour}:{start_time.minute}")

            if difference_days == -1:
                return f"wczoraj o {start_time.hour}:{start_time.minute}"

            if difference_days == 0:
                if difference_hour > 0:
                    if difference_min == 0:
                        return f"za {difference_hour} godzin"
                    if difference_min > 0:
                        return f"za {difference_hour} godzin i {difference_min} min"
                    if difference_min < 0:
                        return f"za {difference_hour - 1} godzin i {60 - abs(difference_min)} min"

                if difference_hour == -1:
                    if difference_min == 0:
                        return f"godzinę temu"

                if difference_hour < 0:
                    if difference_min == 0:
                        return f"{abs(difference_hour)} godziny temu"
                    if difference_min > 0:
                        return f"{abs(difference_hour) - 1} godziny i {60 - abs(difference_min)} minut temu"
                    if difference_min < 0:
                        return f"{abs(difference_hour)} godziny i {abs(difference_min)} minut temu"

                if difference_hour == 0 and difference_min < 0:
                    return f"{abs(difference_min)} minut temu"
                if difference_hour == 0 and difference_min > 0:
                    return f"za {difference_min} minut"

            if difference_days == 1:
                return f"Jutro o godzinie {start_time.hour}:{start_time.minute}"

            if difference_days == 2:
                return f"Pojutrze o godzinie {start_time.hour}:{start_time.minute}"

            if 2 < difference_days < 7:
                return f"w {DNI_TYGODNIA_PL[start_time.weekday()]} o {start_time.hour}:{start_time.minute}"

            if 7 < difference_days < 14:
                if start_time.weekday() in (0, 1, 3, 4):
                    return (
                        f"w przyszły {DNI_TYGODNIA_PL[start_time.weekday()]} o {start_time.hour}:{start_time.minute}")
                if start_time.weekday() in (2, 5, 6):
                    return (
                        f"w przyszłą {DNI_TYGODNIA_PL[start_time.weekday()]} o {start_time.hour}:{start_time.minute}")

            if difference_days > 14 and difference_days != 21 and difference_days != 28:
                return (
                    f"{start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} o {start_time.hour}:{start_time.minute}")

            if difference_days / 7 == 1.0:
                return (
                    f"za tydzień o {start_time.hour}:{start_time.minute}")
            if difference_days / 7 in (2.0, 3.0, 4.0):
                return (
                    f"za {CYFRY_DLA_TYGODNIE_PL[difference_days / 7]} tygodnie o {start_time.hour}:{start_time.minute}")

        if difference_month == 1:

            if difference_days < 0:
                return (
                    f"za {NAZWY_MIESIECY_PL[start_time.month][1] - abs(difference_days)} dni o {start_time.hour}:{start_time.minute}")
            if difference_days == 0:
                return f"za miesiąc o {start_time.hour}:{start_time.minute}"

            if difference_days == 1:
                if difference_hour < 0:
                    return f"za miesiąc i {24 - abs(difference_hour)} godziny"
                if difference_hour == 0:
                    return f"za miesiąc i niecałe {24 - abs(difference_hour)} godziny"
                if difference_hour == 1:
                    return (
                        f"za miesiąc {CYFRY_DLA_TYGODNIE_PL[difference_days]} dzien i {abs(difference_hour)} godzine")
                if 5 > difference_hour > 1:
                    return (
                        f"za miesiąc {CYFRY_DLA_TYGODNIE_PL[difference_days]} dzien i {abs(difference_hour)} godziny")
                if difference_hour >= 5:
                    return (
                        f"za miesiąc {CYFRY_DLA_TYGODNIE_PL[difference_days]} dzien i {abs(difference_hour)} godzin")

            if difference_days == 2:
                if difference_hour <= -1:
                    return f"za miesiąc {difference_days - 1} dzień i {24 - abs(difference_hour)} godziny"

            if 6 >= difference_days > 2:
                if difference_hour <= -1:
                    return f"za miesiąc {difference_days - 1} dni i {24 - abs(difference_hour)} godziny"
                # if difference_hour == -1:
                    # return (f"za miesiąc {difference_days - 1} dni {24 - abs(difference_hour)} godziny")
                if difference_hour == 1:
                    return f"za miesiąc {difference_days} dni i {abs(difference_hour)} godzine"
                if 5 > difference_hour > 1:
                    return f"za miesiąc {difference_days} dni i {abs(difference_hour)} godziny"
                if difference_hour >= 5:
                    return f"za miesiąc {difference_days} dni i {abs(difference_hour)} godzin"

            if difference_days > 6:
                return (
                    f"{start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} o {start_time.hour}:{start_time.minute}")

        if 1 < difference_month <= 4:
            if difference_days == 0:
                return (
                    f"za {CYFRY_DLA_TYGODNIE_PL[difference_month]} miesiące o {start_time.hour}:{start_time.minute}")

        if abs(difference_month) >= 5 and abs(difference_days) >= 0:
            return (
                f"{start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} o {start_time.hour}:{start_time.minute}")

    if difference_year == -1:
        if difference_month == 0:
            if difference_days == 0:
                return f"rok temu o {start_time.hour}:{start_time.minute}"

    if difference_year == 1:
        if difference_month >= 1:
            return f"za rok {start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} o {start_time.hour}:{start_time.minute}"
        if difference_month == 0:
            if difference_days == 0:
                return f"za rok o {start_time.hour}:{start_time.minute}"
            if difference_days == 1:
                if difference_hour >= 0:
                    return f"za rok i {difference_days} dzień"
                if difference_hour < 0:
                    return f"za rok i {24 - abs(difference_hour)} godzin"
            if 7 > difference_days > 1:
                return f"za rok i {difference_days} dni"
            if difference_days >= 7:
                return f"za rok {start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} o {start_time.hour}:{start_time.minute}"

        if difference_month < 0:
            return (
                f"{start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} następnego roku o {start_time.hour}:{start_time.minute}")

    if abs(difference_year) > 1 and abs(difference_month) > 0 and abs(difference_days) >= 1:
        return (
            f"{start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} {start_time.year} o {start_time.hour}:{start_time.minute}")

    if abs(difference_year) > 1 and abs(difference_month) >= 1 and abs(difference_days) >= 0:
        return f"{start_time.day} {NAZWY_MIESIECY_PL[start_time.month][0]} o {start_time.hour}:{start_time.minute}"

if __name__ == '__main__':

    natural_language(start_time=datetime.datetime(2022, 6, 24, 12, 14))