from main import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['axes.unicode_minus']=False
mpl.rcParams['font.sans-serif'] = ['SimHei']
total = 0
iteration = 1
expect_score = 10
target_stat = '火元素伤害加成'
target_part = '杯'
sc = 0

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.08, 1.03*height, '%s' % int(height), size=8, family="Times new roman")

a = np.zeros(55)
for i in range(iteration):
    time = 0
    while(time<10000):
        print(time)

        part = []
        main_stat = ''
        sub_stats = []
        nsub_stats = 0
        val = []
        artifact = Artifact(part=part, main_stat=main_stat, sub_stats=sub_stats, nsub_stats=nsub_stats, val=val)
        create_artifact(artifact)
        sc = int(score(artifact))
        if artifact.main_stat == target_stat and artifact.part == target_part:
            a[sc] = a[sc] + 1
        total = int(a.sum())
        time = time + 1


cm = plt.bar(range(0,55),a,color = "m",width = 0.6)
autolabel(cm)

plt.title('一万次模拟中'+target_stat+target_part+'共出货'+str(total)+"个，其分布如下", fontsize=12)

plt.xlabel("双爆分", fontsize=12)
plt.ylabel("数量", fontsize=12)
plt.yscale("log")
plt.show()


    #total = total + time
    #avg = total/iteration
    #print("双爆{}分圣遗物次数期望：{}，概率：{:.8f}%，消耗树脂期望：{:.2f}，大约需要{:.2f}天".format(expect_score,avg,1/avg*100,avg*18.69,avg*18.69/180))
