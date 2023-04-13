from main import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['axes.unicode_minus']=False
mpl.rcParams['font.sans-serif'] = ['SimHei']
iteration = 150


total = 0
y = []
x = []
for i in range(iteration):
    a = 0
    for j in range(5):
        time = 0
        gobletscore = 0
        crownscore = 0
        plumescore = 0
        sandscore = 0
        flowerscore = 0
        while(time < 30*i):
            print(time)
            part = []
            main_stat = ''
            sub_stats = []
            nsub_stats = 0
            val = []
            artifact = Artifact(part=part, main_stat=main_stat, sub_stats=sub_stats, nsub_stats=nsub_stats, val=val)
            create_artifact(artifact)
            sc = int(score(artifact))
            if artifact.part == '头' and artifact.main_stat == '暴击率':
                crownscore = max(sc+66.2,crownscore)
            if artifact.part == '花':
                flowerscore = max(sc,flowerscore)
            if artifact.part == '毛':
                plumescore = max(sc,plumescore)
            if artifact.part == '沙' and artifact.main_stat == '大攻击':
                sandscore = max(sc,sandscore)
            if artifact.part == '杯' and artifact.main_stat == '火元素伤害加成':
                gobletscore = max(sc,gobletscore)
            time = time + 1
        total = sandscore + crownscore + plumescore + gobletscore + flowerscore
        a = a + total

    total = a/5
    y.append(total)
    x.append(4*i)
    print(total,sandscore,crownscore,plumescore,gobletscore,flowerscore)

plt.scatter(x, y, color="m")
poly = np.polyfit(x, y, deg=5)
y = np.polyval(poly, x)
plt.plot(x, y)


plt.title('圣遗物双爆分与坐牢时长关系')

plt.xlabel("坐牢时长(天)", fontsize=12)
plt.ylabel("双爆分", fontsize=12)
plt.legend()
plt.show()