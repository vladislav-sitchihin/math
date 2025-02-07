#Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
#По формуле Бернулли
from math import factorial as f 
from math import e
print((f(100)/(f(85)*f(15)))*0.8**85*0.2**15)

#Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. В жилом комплексе после ремонта в один день включили 5000 новых лампочек. Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
#Распределение Пуассона, p = 0.0004, n = 5000, m1 = 0, m2 = 2
l = 0.0004*5000
Pm1 = (l**0/f(0))*e**(-l)
Pm2 = (l**2/f(2))*e**(-l)
print(Pm1, Pm2)

#Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
#По формуле Бернулли
print((f(144)/(f(70)*f(74)))*0.5**70*0.5**74)

#В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча.  
#1)Какова вероятность того, что все мячи белые?

# Число сочетаний 2 белых из 7 белых в первом ящике =
C1 = f(7)/(f(2)*f(5))
# Число сочетаний 2 белых из 10 мячей в первом ящике =
C2 = f(10)/(f(2)*f(8))

# То же самое для 2-го ящика
C3 = f(9)/(f(2)*f(7))
C4 = f(11)/(f(2)*f(9))
# Ответ
print(f"вероятность того, что все мячи белые - {(C1/C2)*(C3/C4)}")
#2)Какова вероятность того, что ровно два мяча белые? 
#Возможные комбинации - 2 белых из 1 ящика, 2 белых из второго, по одному белому. Общая вероятность события - сумма этих 3 возможностей
#P1
C5 = f(2)/(f(2)*f(0))
P1 = (C1/C2)*(C5/C4)
#P2
C6 = f(3)/(f(2)*f(1))
P2 = (C6/C2)*(C3/C4)
#P3
P3 = ((f(7)/(f(1)*f(6))*f(3)/(f(1)*f(2)))/C2)*((f(9)/(f(1)*f(8))*f(2)/(f(1)*f(1)))/C4)
print(f"промежуточные ответы - {P1}, {P2}, {P3}")
# Ответ
print(f"вероятность того, что ровно два мяча белые - {P1+P2+P3}")
#3)Какова вероятность того, что хотя бы один мяч белый? 1 - P(2 и 2 черные)
print(f"вероятность того, что хотя бы один мяч белый - {1-(C6/C2)*(C5/C4)}")
