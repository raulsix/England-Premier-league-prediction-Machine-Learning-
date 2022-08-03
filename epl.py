import joblib

name=['Brentford', 'Man United' ,'Burnley', 'Chelsea', 'Everton' ,'Leicester'
, 'Watford', 'Norwich' ,'Newcastle', 'Tottenham', 'Liverpool', 'Aston Villa'
, 'Crystal Palace', 'Leeds', 'Man City', 'Brighton' ,'Southampton', 'Wolves'
, 'Arsenal', 'West Ham', 'Bournemouth', 'Sheffield United']
num=-1
for i in name:
    num=num+1
    numx=(str(num)+".")
    print(numx,i)
print()   
hteam=int(input("Enter Home Team:.."))
ateam=int(input("Enter Away Team:.."))


x=joblib.load("eplpredictor.pkl")
x=x.predict([[hteam,ateam]])
hteam=name[hteam]
ateam=name[ateam]

result=int(x[0])
if result == 1:
    print(hteam," Vs ",ateam)
    print('Winner Will be',hteam)
elif result == 2:
    print(hteam," Vs ",ateam)
    print('Winner Will be',ateam)
else:
    print(hteam," Vs ",ateam)
    print('Draw awaits')
    

