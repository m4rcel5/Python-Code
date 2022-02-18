"""
    @author: m4rcel5
    19.02.2022
    Time table
"""
import os
import time


# This functin allows the user to enter the hours of each school day
# IN: ---
# OUT: times (list)
def time_table():
    lst = []
    times = []
    week_days = ('Monday?', 'Tuesday?', 'Wednesday?', 'Thursday?', 'Friday?')
    i = 0
    while i < len(week_days):
        print('How much hours you spent in school on',week_days[i])
        try:
            hours = int(input('(Maximum: 12 and Minimum: 1): '))
            os.system('cls')
            if hours >= 1 and hours <= 12:
                times.append(hours)
                i += 1
            else:
                print('Thats not a possible answer of school hours!')
                time.sleep(2)
                print('Only a maximum of 12 hours and a minimum of 1 hour')
                time.sleep(2)
                os.system('cls')
        except:
            print("Thats not a possible answer of school hours!")
            time.sleep(1)
            print("Only numbers allowed with a maximum of 12 and a minimum of 1 hour")
            time.sleep(3)
            os.system('cls')
    lst.append(times)
    return lst


# The user can enter the subjects for each day
# IN: hour_lst (list)
# OUT: ---
def subject_table(hour_lst):
    hour_list = hour_lst
    day_lst = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    j = 0
    for hour in hour_lst[0]:
        i = 0
        subject_lst = []
        while i < hour:
            print('Here you can enter the name of the subject in a shorter version (z.b. German = G, maximum = 5 chars),',day_lst[j])
            subject = input(': ')
            os.system('cls')
            if len(subject) <= 5:
                subject_lst.append(subject.upper())
                i += 1
            else:
                print('The name that you entered is too long! (maximum = 5 chars)')
                time.sleep(1)
                print('Please try again')
                time.sleep(1)
                os.system('cls')
        hour_list.append(subject_lst)
        j += 1
    hour_list.pop(0)
    return hour_list


# This function asks the user if he want to save the Time Table in a CSV-File at the path C:\temp
# IN: subjects (list)
# OUT: ---
def save_file(subjects):
    question = input("Do you want to save your Time Table in a CSV-File (Y/N)?: ")
    asking = question.casefold()
    while asking != "no" and asking != "n" and asking != "yes" and asking != "y":
        print("Not accepted input!")
        time.sleep(1)
        print("Try it again")
        time.sleep(1)
        os.system('cls')
        question = input("Do you want to save your Time Table in a CSV-File (Y/N)?: ")
        asking = question.casefold()
    if asking == "yes" or asking == "y":
        try:
            existend = os.path.isfile("c:\\temp\\Time_Table.csv")
            if not existend:
                File = open('c:\\temp\\Time_Table.csv','wt', encoding = 'utf-8-sig')
                File.write('Monday;Tuesday;Wednesday;Thursday;Friday\n')
                File.close()
                print('The file was created succesfully!')
                File = open('c:\\temp\\Time_Table.csv','a+', encoding = 'utf-8-sig')
                i_t = False
                j_t = False
                k_t = False
                l_t = False
                m_t = False
                j = 0
                k = 0
                l = 0
                m = 0
                n = 0
                while not i_t or not j_t or not k_t or not l_t or not m_t:
                    i = 0
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][j]) + ';')
                        i += 1
                    elif i_t:
                        File.write(';')
                        i += 1
                    else:
                        i_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][k]) + ';')
                        i += 1
                    elif j_t:
                        File.write(';')
                        i += 1
                    else:
                        j_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][l]) + ';')
                        i += 1
                    elif k_t:
                        File.write(';')
                        i += 1
                    else:
                        k_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][m]) + ';')
                        i += 1
                    elif l_t:
                        File.write(';')
                        i += 1
                    else:
                        l_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][n]) + ';')
                        i += 1
                    elif m_t:
                        File.write(';')
                        i += 1
                    else:
                        m_t = True
                        File.write(';')
                        i += 1
                    File.write('\n')
                    j += 1
                    k += 1
                    l += 1
                    m += 1
                    n += 1 
                File.close()
                os.system('cls')
            else:
                File = open('c:\\temp\\Time_Table.csv','a+', encoding = 'utf-8-sig')
                File.write('Monday;Tuesday;Wednesday;Thursday;Friday\n')
                i_t = False
                j_t = False
                k_t = False
                l_t = False
                m_t = False
                j = 0
                k = 0
                l = 0
                m = 0
                n = 0
                while not i_t or not j_t or not k_t or not l_t or not m_t:
                    i = 0
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][j]) + ';')
                        i += 1
                    elif i_t:
                        File.write(';')
                        i += 1
                    else:
                        i_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][k]) + ';')
                        i += 1
                    elif j_t:
                        File.write(';')
                        i += 1
                    else:
                        j_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][l]) + ';')
                        i += 1
                    elif k_t:
                        File.write(';')
                        i += 1
                    else:
                        k_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][m]) + ';')
                        i += 1
                    elif l_t:
                        File.write(';')
                        i += 1
                    else:
                        l_t = True
                        File.write(';')
                        i += 1
                    if j < len(subjects[i]):
                        File.write(str(subjects[i][n]) + ';')
                        i += 1
                    elif m_t:
                        File.write(';')
                        i += 1
                    else:
                        m_t = True
                        File.write(';')
                        i += 1
                    File.write('\n')
                    j += 1
                    k += 1
                    l += 1
                    m += 1
                    n += 1 
                File.close()
        except:
            print("Oops, there was an error!")
            time.sleep(1)
            print("The file cant be created :(")
    else:
        return


# This function generates a time-table with all the informations
# IN: hours_subjects (list)
# OUT: ---
def create_time_table(hours_subjects):
    subject_length = 5 * ' '
    print(31 * '-')
    print('| MON | TUE | WED | THUR| FRI |')
    print(31 * '-')
    j_t = False
    k_t = False
    l_t = False
    m_t = False
    n_t = False
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    while not j_t or not k_t or not l_t or not m_t or not n_t:
        i = 0
        if j < len(hours_subjects[i]):
            print('|' + (hours_subjects[i][j] + ((len(subject_length) - len(hours_subjects[i][j]))) * ' '), end='|')
            i += 1
        elif j_t:
            print('|' + 5 * ' ',end='|')
            i += 1
        else:
            j_t = True
            print('|' + 5 * ' ',end='|')
            i += 1
        if k < len(hours_subjects[i]):
            print(hours_subjects[i][k] + ((len(subject_length) - len(hours_subjects[i][k])) * ' '), end='|')
            i += 1
        elif k_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            k_t = True
            print(5 * ' ',end='|')
            i += 1
        if l < len(hours_subjects[i]):
            print(hours_subjects[i][l] + ((len(subject_length) - len(hours_subjects[i][l])) * ' '), end='|')
            i += 1
        elif l_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            l_t = True
            print(5 * ' ',end='|')
            i += 1
        if m < len(hours_subjects[i]):
            print(hours_subjects[i][m] + ((len(subject_length) - len(hours_subjects[i][m])) * ' '), end='|')
            i += 1
        elif m_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            m_t = True
            print(5 * ' ',end='|')
            i += 1
        if n < len(hours_subjects[i]):
            print(hours_subjects[i][n] + ((len(subject_length) - len(hours_subjects[i][n])) * ' '), end='|')
            i += 1
        elif  n_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            n_t = True
            print(5 * ' ',end='|')
            i += 1
        print('')
        j += 1
        k += 1
        l += 1
        m += 1
        n += 1
    print(31 * '-')
    return



# ===============================================================================================================================================
# ================================================================= MAIN ========================================================================
# ===============================================================================================================================================
os.system('cls')
hour_table = time_table()
subjects_and_hours = subject_table(hour_table)
os.system('cls')
save_file(subjects_and_hours)
os.system('cls')
create_time_table(subjects_and_hours)