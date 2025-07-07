import sqlite3
conn = sqlite3.connect('football_db.sqlite3.sqlite3')




#ამით ბაზიდან გამოგვაქვს მხოლოდ ის ფეხბურთელები, რომლებიც ინგლისიდან არიან.
cursor = conn.cursor()
#language=SQL
res_select = cursor.execute("SELECT * FROM football WHERE nationality='England'")
# print(res_select)
results = cursor.fetchall()
for each in results:
    print(each)


#
u_name = input('enter name: ')
u_fullname = input('enter full name: ')
u_bdate = input('enter birth date: ')
u_age = input('enter age: ')
u_height = input('enter height in cm: ')
u_weight = input('enter weight in kgs: ')
u_position = input('enter position: ')
u_nationality = input('enter nationality: ')
u_rating = input('enter overall rating: ')
u_potential = input('enter potential: ')


#ცხრილში რომ გვაქვს მონაცემები, მაგას ვამატებთ, მაღლა ოცემულ მონაცემებს, რომლებიც მომხმარებელს input ით შეყავს.
#language=SQL
cursor.execute("INSERT INTO football (name,fullname,bdate,age,height,weight,position,nationality,rating,potential) VALUES (?,?,?,?,?,?,?,?,?,?)"
,(u_name, u_fullname, u_bdate, u_age, u_height, u_weight, u_position, u_nationality, u_rating, u_potential
  ))


#აქ უკვე ვანახლებთ ბაზას და ვცვლით მონაცემს, სადაც nationality გერმანიაა მომხმარებლიოს შეყვანილი მონაცემით.
#language=SQL
cursor.execute("UPDATE football SET name=?, fullname=?, bdate=?, age=?, height=?, weight=?, position=?, nationality=?, rating=?, potential=? WHERE nationality='German'",
(u_name, u_fullname, u_bdate, u_age, u_height, u_weight, u_position, u_nationality, u_rating, u_potential
  ))

#ბაზიდან წავშლით იმ სახელს რომელსაც მომხმარებელი შეიყვანს
name = input('შეიყვანეთ ფეხბურთელის სახელი: ')
#language=SQL
cursor.execute('DELETE FROM football WHERE name=?', (name,))

print(f'{name} წარმატებით წაიშალა!')

#language=SQL
res = cursor.execute("SELECT * FROM football")
for each in res:
    print(each)


#გრაფა პირველი: ასაკის მიხედვით დიაგრამაზე პროცენტის ასახვა
#პროცენტის ასახვისთვის ვწერთ:

#language=SQL
def count_age(age):
    return cursor.execute('SELECT count(*) FROM football WHERE age=?', (age,)).fetchone()[0]
def percentage(age,sum):
    return age/100*sum


c_twentyone = count_age("21")
c_twentythree = count_age("23")
c_twentyfour = count_age("24")
c_twentyseven = count_age("27")
c_other = (
    count_age('17')+
    count_age('18')+
    count_age('19')+
    count_age('20')+
    count_age('25')+
    count_age('28')+
    count_age('30')
)
l = ['21', '23', '24', '27', 'other']
s = [c_twentyone, c_twentythree, c_twentyfour, c_twentyseven, c_other]



import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.pie(sizes, labels=l, autopct='%.1f%%',startrangle=90)
plt.show()


#გრაფა მეორე, სადაც ნაჩვენებია თუ რომელი ქვეყნიდან რამდენი ფეხბურთელია.
fig, ax = plt.subplots()

nationality = ['England', 'Germany', 'Italy', 'Brazil', 'France']
#language=SQL
def c_nationality(nationality):
    return cursor.execute('SELECT count(*) FROM football WHERE nationality=?', (nationality,)).fetchone()[0]


c1 = c_nationality('England')
c2 = c_nationality('Germany')
c3 = c_nationality('Italy')
c4 = c_nationality('Brazil')
c5 = c_nationality('France')

counts = [c1,c2,c3,c4,c5]
bar_l = ['England', 'Germany', 'Italy', 'Brazil', 'France']
bar_col = ['tab:green', 'tab:red', 'tab:yellow', 'tab:blue', 'tab:orange']

ax.bar(nationality, counts, lable=bar_l, color=bar_col)

ax.set_ylabel('ფეხბურთელები')
ax.set_title('წარმომავლობა')

plt.show()


#გრაფა მესამე, სადაც ნაჩვენებია სიმაღლის ცვლილება მოცემულ ფეხბურთელებში 173-187 სანტიმეტრი.
#language=SQL
def count_height(height):
    return cursor.execute('SELECT count(*) FROM football WHERE height=?' (height,)).fetchone()[0]

h1 = count_height(173)
h2 = count_height(187)
x = [173,187]
y = [h1,h2]

plt.plot(x,y)
plt.title('სიმაღლის ცვლილება 173სმ-დან 187სმ-მდე')
plt.xlabel('სანტიმეტრები')
plt.ylabel('ცვლილება')

plt.show()


conn.commit()
conn.close()

