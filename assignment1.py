#----------------------------------------------------
# assignment 1: Mini bear-tracks
# Purpose of code:
#
# Author: Daniel Akanmu
# Collaborators/references: None
#----------------------------------------------------

def getData(filename1, filename2, filename3):
    '''
    This function will read the files courses.txt, students.txt, enrollment.txt
    and return it's contents in an organized list.
    parameters: filename1, filename2, filename3
    return: list1, list2, list3
    '''
    
#-------------------------------------------------------------------------------    
    #Courses:
    data = []
    fin = open(filename1, 'r')
    fileContents = fin.readlines()
    for line in fileContents:
        line = line.strip()  
        data.append(line.split(';'))
    fin.close()
    for x in range (len(data)):
        for y in range(4):
            data[x][y] = data[x][y].strip()
#-------------------------------------------------------------------------------
    #students:
    data2 = []
    fin = open(filename2, 'r')
    fileContents = fin.readlines()
    for line in fileContents:
        line = line.strip()  
        data2.append(line.split(','))
    fin.close()
    for x in range (len(data2)):
        for y in range(3):
            data2[x][y] = data2[x][y].strip()
#-------------------------------------------------------------------------------
    #enrollment:
    data3 = []
    fin = open(filename3, 'r')
    fileContents = fin.readlines()
    for line in fileContents:
        line = line.strip()
        data3.append(line.split(':'))
    fin.close()
    for x in range (len(data3)):
        for y in range(2):
            data3[x][y] = data3[x][y].strip()    
#-------------------------------------------------------------------------------
    return data, data2, data3  

#===============================================================================
def dic(list1, list2, enr):
    '''
    This function will convert the lists (courses.txt and student.txt) into 
    dictonaries. 
    parameters: list1, list2, enr
    return: courses, students
    '''
    courses = {}
    students = {}
    
    for i in range (len(list1)):
        list1[i][2] = int(list1[i][2])
        #list1[i][1] = (list1[i][1]).split(' ')
        courses[list1[i][0]] = list1[i][1:len(list1[0])]
    
    for i in range (len(list2)):
        students[list2[i][0]] = list2[i][1:len(list2[0])] 
    
    for x in range(len(enr)):
        try:
            courses[enr[x][0]]
            courses[enr[x][0]][1] -= 1
        except:
            courses[enr[x][0]][1] -= 0
    
    
    return courses, students


def getAction():
    '''
    The function will get the input of the user and check if it is valid. It
    will return the user's input if valid.
    parameters: None
    return: Choice
    '''
    x = True
    
    print("\nWhat would you like to do?")
    print("1. Print timetable")
    print("2. Enroll in course")
    print("3. Drop course")
    print("4. Quit")
    choice = input("> ")
    
    while( x == True):
        choice = choice.strip()
        if choice == '1':
            x = False
        elif choice == '2':
            x = False
        elif choice == '3':
            x = False
        elif choice == '4':
            x = False  
        else:
            print("Sorry, invalid entry. Please enter a choice from 1 to 4.")
            choice = input("> ")
    
    return choice  
#===============================================================================


def showTable(cor, stu, enr):
    '''
    The function will print out the timetable depending on the student ID. 
    parameters: cor, stu, enr
    return: None
    '''
    sId = input("\nStudent ID: ")
    courseTaken = []
    try:
        stu[sId]
        print("Timetable for" , (stu[sId][1]).upper() + ", in the faculty of", stu[sId][0] )
    except:
        print("Invalid student ID. Cannot print timetable.")
        return 
    
    for x in range(len(enr)):
        if sId == enr[x][1]:
            courseTaken.append(enr[x][0])
            
    n = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
        '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30']    
    
    t8 = []
    t11 = []
    t14 = []
    
    for k in courseTaken:
        if '8:00' in cor[k][0]:
            t8.append(k)
        if '11:00' in cor[k][0]:
            t11.append(k)
        if '14:00' in cor[k][0]:
            t14.append(k)
    
    print('          Mon        Tues         Wed        Thurs       Fri')
    print("     "+('+-----------' * 5) + '+')    
    for x in range (len(n)):
        def func():
            for y in range(len(courseTaken)):
                if n[x] in cor[courseTaken[y]][0]:
                    if courseTaken[y] in t8 and len(t8) > 1:
                        courseTaken.remove(t8[0])
                        courseTaken.remove(t8[1])
                        if 'MWF' in cor[t8[0]][0]:
                            print("{:<5}|".format(n[x]), end = '')
                            print(' {:^9} '.format(t8[0]) + "|", end = '')
                            print(' {:^9} '.format(t8[1]) + "|", end = '')
                            print(' {:^9} '.format(t8[0]) + "|", end = '')
                            print(' {:^9} '.format(t8[1]) + "|", end = '')
                            print(' {:^9} '.format(t8[0]) + "|")
                            
                            print(f"     |" , "{:>6}    ".format(cor[t8[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[0]][1]) + "|")
                            
                            print(f"     |"+("           |")*5)
                        else:
                            print("{:<5}|".format(n[x]), end = '')
                            print(' {:^9} '.format(t8[1]) + "|", end = '')
                            print(' {:^9} '.format(t8[0]) + "|", end = '')
                            print(' {:^9} '.format(t8[1]) + "|", end = '')
                            print(' {:^9} '.format(t8[0]) + "|", end = '')
                            print(' {:^9} '.format(t8[1]) + "|")
                            
                            print(f"     |" , "{:>6}    ".format(cor[t8[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t8[1]][1]) + "|")
                            
                            print(f"     |"+("           |")*5)                            
                            
                        return
                    
                    elif courseTaken[y] in t11 and len(t11) > 1:
                        courseTaken.remove(t11[0])
                        courseTaken.remove(t11[1])
                        if 'MWF' in cor[t11[0]][0]:
                            print("{:<5}|".format(n[x]), end = '')
                            print(' {:^9} '.format(t11[0]) + "|", end = '')
                            print(' {:^9} '.format(t11[1]) + "|", end = '')
                            print(' {:^9} '.format(t11[0]) + "|", end = '')
                            print(' {:^9} '.format(t11[1]) + "|", end = '')
                            print(' {:^9} '.format(t11[0]) + "|")
                            
                            print(f"     |" , "{:>6}    ".format(cor[t11[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t11[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t11[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t11[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t11[0]][1]) + "|")
                            
                            print(f"     |"+("           |")*5)
                        else:
                            print("{:<5}|".format(n[x]), end = '')
                            print(' {:^9} '.format(t11[1]) + "|", end = '')
                            print(' {:^9} '.format(t11[0]) + "|", end = '')
                            print(' {:^9} '.format(t11[1]) + "|", end = '')
                            print(' {:^9} '.format(t11[0]) + "|", end = '')
                            print(' {:^9} '.format(t11[1]) + "|")
                            
                            print(f"     |" , "{:^} |".format(cor[t11[1]][1]) , end = '')
                            print(" {:^9} ".format(cor[t11[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t11[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t11[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t11[1]][1]) + "|")
                            
                            print(f"     |"+("           |")*5)                            
                            
                        return 
                    elif courseTaken[y] in t14 and len(t14) > 1:
                        courseTaken.remove(t14[0])
                        courseTaken.remove(t14[1])
                        if 'MWF' in cor[t14[0]][0]:
                            print("{:<5}|".format(n[x]), end = '')
                            print(' {:^9} '.format(t14[0]) + "|", end = '')
                            print(' {:^9} '.format(t14[1]) + "|", end = '')
                            print(' {:^9} '.format(t14[0]) + "|", end = '')
                            print(' {:^9} '.format(t14[1]) + "|", end = '')
                            print(' {:^9} '.format(t14[0]) + "|")
                            
                            print(f"     |" , "{:>6}    ".format(cor[t14[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[0]][1]) + "|")
                            
                            print(f"     |"+("           |")*5)
                        else:
                            print("{:<5}|".format(n[x]), end = '')
                            print(' {:^9} '.format(t14[1]) + "|", end = '')
                            print(' {:^9} '.format(t14[0]) + "|", end = '')
                            print(' {:^9} '.format(t14[1]) + "|", end = '')
                            print(' {:^9} '.format(t14[0]) + "|", end = '')
                            print(' {:^9} '.format(t14[1]) + "|")
                            
                            print(f"     |" , "{:>6}    ".format(cor[t14[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[1]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[0]][1]) + "|", end = '')
                            print(" {:^9} ".format(cor[t14[1]][1]) + "|")
                            
                            print(f"     |"+("           |")*5)                            
                            
                        return                                        
                            
                    elif 'MWF' in cor[courseTaken[y]][0]:
                        print("{:<5}|".format(n[x]), end = '')
                        print(' {:^9} '.format(courseTaken[y]) + "|", end = '')
                        print('           |', end = '')
                        print(' {:^9} '.format(courseTaken[y]) + "|", end = '')
                        print('           |', end = '')
                        print(' {:^9} '.format(courseTaken[y]) + "|")
                        print(f"     |" , "{:^9} |".format(cor[courseTaken[y]][1]) , end = '')
                        print('           |', end = '')
                        print(" {:^9} ".format(cor[courseTaken[y]][1]) + "|", end = '')
                        print('           |', end = '')
                        print(" {:^9} ".format(cor[courseTaken[y]][1]) + "|")
                        if x == 2 or x == 8 or x == 14:
                            print(f"     |           |", end = '')
                            print("-----------|", end = '')
                            print("           |", end = '')
                            print("-----------|", end = '')
                            print("           |")
                        else:
                            print(f"     |"+("           |")*5) 
                            
                        return
                   
                    elif 'TR' in cor[courseTaken[y]][0]:
                        print("{:<5}|".format(n[x]), end='')
                        print('           ', end = '')
                        print('| {:^9} |'.format(courseTaken[y]) , end = '')
                        print('           ', end = '')
                        print('| {:^9} |'.format(courseTaken[y]) , end = '')
                        print('           |')
                        print(f"     |", end = '' )
                        print('           |', end = '')
                        print(" {:^9} ".format(cor[courseTaken[y]][1]) + "|", end = '')
                        print('           |', end = '')
                        print(" {:^9} ".format(cor[courseTaken[y]][1]) + "|", end = '')
                        print('           |')
                        if x%2 != 0 and (x != 5 and x != 11 and x != 17):
                            print(f"     |-----------|", end = '')
                            print("           |", end = '')  
                            print("-----------|", end = '')
                            print("           |", end = '')  
                            print("-----------|")
                        else:
                            print(f"     |"+("           |")*5) 
                        return
            if x%2 != 0 and (x != 5 and x != 11 and x != 17):
                print("{:<5}|".format(n[x]), end = '')
                print("           |"*5)
                print(f"     |"+("           |")*5)
                print(f"     |-----------|", end = '')
                print("           |", end = '')
                print(f"-----------|", end = '')
                print("           |", end = '')  
                print(f"-----------|") 
            elif x == 2 or x == 8 or x == 14:
                print("{:<5}|".format(n[x]), end = '')
                print("           |"*5)
                print(f"     |"+("           |")*5)
                print("     |           |", end = '')
                print(f"-----------|", end = '')
                print("           |", end = '') 
                print(f"-----------|", end = '')
                print(f"           |")     
            elif x == 5 or x == 11 or x == 17:
                print("{:<5}|".format(n[x]), end = '')
                print("           |"*5)
                print(f"     |"+("           |")*5)
                print(f"     +"+("-----------+")*5)            
            else:
                print("{:<5}|".format(n[x]), end = '')
                print("           |"*5)
                print(f"     |"+("           |")*5)
                print(f"     |"+("           |")*5) 
        func()    
    
#===============================================================================
def enrollCourse(cor, stu, enr):
    '''
    This Function will update the enrollment list and add courses to it. It will
    also update the enrollment.txt.
    parameters: cor, stu, enr
    return: enr
    '''
    courseTaken = []
    sId = input("\nStudent ID: ")
    try:
        stu[sId]
    except:
        print("Invalid student ID. Cannot continue with course enrollment.")
        return enr
    
    cName = input("Course name: ")
    cName = cName.upper()
    try:
        cor[cName]
    except:
        print("Invalid course name.")
        return enr
    
    for x in range(len(enr)):
        if sId == enr[x][1]:
            courseTaken.append(enr[x][0])   
            
    
    
    if cName in courseTaken:
        print("Schedule conflict: already registered for course on " + cor[cName][0])
        return enr
    elif cor[cName][1] == 0:
        print("Cannot enroll.", cName, "is already at capacity.", end = ' ') 
        print("Please contact advisor to get on waiting list.") 
        return enr
    elif not cName in courseTaken and cor[cName][1] != 0:
        for x in courseTaken:
            if cor[cName][0] == cor[x][0]:
                print("Schedule conflict: already registered for course on " + cor[x][0])
                return enr  
    
    if not cName in courseTaken:
        print(stu[sId][1], "has successfully been enrolled in", cName + ", on", cor[cName][0])
        enr.append([cName, sId])
        cor[cName][1] -= 1
        
        fin = open("enrollment.txt", 'w')
        for x in range (len(enr)):
            fin.write(f"{enr[x][0]}: {enr[x][1]}\n")
        fin.close()        
    
        return enr
    
def dropCourse(cor, stu, enr):
    '''
    This Function will update the enrollment list and remove courses in it. It 
    will also update the enrollment.txt.
    parameters: cor, stu, enr
    return: enr
    '''
    courseTaken = []
    sId = input("\nStudent ID: ")
    try:
        stu[sId]
    except:
        print("Invalid student ID. Cannot continue with course drop.")
        return enr
    for x in range(len(enr)):
        if sId == enr[x][1]:
            courseTaken.append(enr[x][0]) 
    
    courseTaken = sorted(courseTaken)
    print("Select course to drop:")
    for x in courseTaken:
        print("-", x)
    cName = input("> ")
    cName = cName.upper()
    try:
        cor[cName]
        enr.remove([cName, sId])
        cor[cName][1] += 1
        print(stu[sId][1], "has successfully dropped", cName)
    
        fin = open("enrollment.txt", 'w')
        for x in range (len(enr)):
            fin.write(f"{enr[x][0]}: {enr[x][1]}\n")
        fin.close()
        
        return enr
    except:
        print("Drop failed.", stu[sId][1], "is not currently registered in", cName)
        return enr

#===============================================================================

def main():
    print("\n==========================")
    print("Welcome to Mini-BearTracks")
    print("==========================")
    list1, list2, enroll = getData("courses.txt", "students.txt", "enrollment.txt")
    courses, students = dic(list1, list2, enroll)
    
    
    quit = False
    
    while not quit: 
        action = getAction()
    
        if action == '1':
            showTable(courses,students,enroll)
        elif action == '2':
            enroll = enrollCourse(courses,students,enroll)
        elif action == '3':
            enroll = dropCourse(courses,students,enroll)
        elif action == '4':
            quit = True
    
    print('Goodbye')      
    
    



if __name__ == '__main__':
    main()
    