import numpy as np
import random

# 圣遗物类
class Artifact:
    def __init__(self, part, main_stat, sub_stats,nsub_stats,val):
        self.part = part
        self.main_stat = main_stat
        self.sub_stats = sub_stats
        self.nsub_stats = nsub_stats
        self.val = val

    def print_Fin_info(self):
        print("强化后：")
        print(f"部位：{self.part}")
        print(f"主属性：{self.main_stat}")
        print("副属性：")
        for i in range(0, 4):
            if self.sub_stats[i] == '小防御':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            elif self.sub_stats[i] == '元素精通':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            elif self.sub_stats[i] == '小生命':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            elif self.sub_stats[i] == '小攻击':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            else:
                print("{}: +{:.1f}%".format(self.sub_stats[i], self.val[i]))


    def print_Ini_info(self):
        print("胚子：")
        print(f"部位：{self.part}")
        print(f"主属性：{self.main_stat}")
        print("副属性：")
        for i in range(0, self.nsub_stats):
            if self.sub_stats[i] == '小防御':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            elif self.sub_stats[i] == '元素精通':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            elif self.sub_stats[i] == '小生命':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            elif self.sub_stats[i] == '小攻击':
                print("{}: +{:.1f}".format(self.sub_stats[i], self.val[i]))
            else:
                print("{}: +{:.1f}%".format(self.sub_stats[i], self.val[i]))

# 模拟强化函数
def simulate_enhancement(artifact):
    n = artifact.nsub_stats
    enhance_chance = artifact.nsub_stats + 1
    while n <= 3:
        new_stat = random.choices(
            ['大攻击', '大防御', '大生命', '小攻击', '小生命', '小防御', '暴击率', '暴击伤害', '元素充能', '元素精通'],
            [0.0968, 0.0968, 0.0968, 0.129, 0.129, 0.129, 0.0645, 0.0645, 0.0968, 0.0968], k=1)
        tmp = new_stat
        tmp = ''.join(str(i) for i in tmp)  #先把新属性拆成字符串，方便匹配
        Tmp = [token for st in artifact.sub_stats for token in st]
        if tmp != artifact.main_stat and tmp not in Tmp:
            artifact.sub_stats.append(new_stat)
            n = n + 1


    #先初始化

    artifact.sub_stats = [token for st in artifact.sub_stats for token in st]
    for stat in artifact.sub_stats:

        if stat == '小生命':
            artifact.val.append(random.choice([209,239,269,299]))
        if stat == '暴击率':
            artifact.val.append(random.choice([2.7,3.1,3.5,3.9]))
        if stat == '暴击伤害':
            artifact.val.append(random.choice([5.4,6.2,7.0,7.8]))
        if stat == '大攻击':
            artifact.val.append(random.choice([4.1,4.7,5.3,5.8]))
        if stat == '大生命':
            artifact.val.append(random.choice([4.1, 4.7, 5.3, 5.8]))
        if stat == '大防御':
            artifact.val.append(random.choice([5.1,5.8,6.6,7.3]))
        if stat == '小攻击':
            artifact.val.append(random.choice([14,16,18,19]))
        if stat == '元素精通':
            artifact.val.append(random.choice([16, 19, 21, 23]))
        if stat == '小防御':
            artifact.val.append(random.choice([16, 19, 21, 23]))
        if stat == '元素充能':
            artifact.val.append(random.choice([4.5,5.2,5.8,6.5]))


    for i in range(1,enhance_chance+1):
        num = random.choice([0,1,2,3])
        stat = artifact.sub_stats[num]
        if stat == '小生命':
            artifact.val[num] = artifact.val[num] + random.choice([209, 239, 269, 299])
        if stat == '暴击率':
            artifact.val[num] = artifact.val[num] + random.choice([2.7, 3.1, 3.5, 3.9])
        if stat == '暴击伤害':
            artifact.val[num] = artifact.val[num] + random.choice([5.4, 6.2, 7.0, 7.8])
        if stat == '大攻击':
            artifact.val[num] = artifact.val[num] + random.choice([4.1, 4.7, 5.3, 5.8])
        if stat == '大生命':
            artifact.val[num] = artifact.val[num] + random.choice([4.1, 4.7, 5.3, 5.8])
        if stat == '大防御':
            artifact.val[num] = artifact.val[num] + random.choice([5.1, 5.8, 6.6, 7.3])
        if stat == '小攻击':
            artifact.val[num] = artifact.val[num] + random.choice([14, 16, 18, 19])
        if stat == '元素精通':
            artifact.val[num] = artifact.val[num] + random.choice([16, 9, 21, 23])
        if stat == '小防御':
            artifact.val[num] = artifact.val[num] + random.choice([16, 19, 21, 23])
        if stat == '元素充能':
            artifact.val[num] = artifact.val[num] + random.choice([4.5, 5.2, 5.8, 6.5])


def score(artifact):
    score = 0
    for stat in artifact.sub_stats:
        if stat == '暴击率':
            score = score + artifact.val[artifact.sub_stats.index(stat)] * 2
        if stat == '暴击伤害':
            score = score + artifact.val[artifact.sub_stats.index(stat)]
    return score


def create_sub_stat(artifact):
    while len(artifact.sub_stats) < artifact.nsub_stats:
        new_stat = random.choices(['大攻击', '大防御', '大生命', '小攻击','小生命','小防御','暴击率','暴击伤害', '元素充能','元素精通'],
                                  [0.0968,0.0968,0.0968,0.129,0.129,0.129,0.0645,0.0645,0.0968,0.0968],k=1)

        tmp = new_stat
        tmp = ''.join(str(i) for i in tmp)  #先把新属性拆成字符串，方便匹配
        Tmp = [token for st in artifact.sub_stats for token in st]
        if tmp != artifact.main_stat and tmp not in Tmp:
            artifact.sub_stats.append(new_stat)

def create_artifact(artifact):
    artifact.part = random.choice(['花', '毛', '头', '杯', '沙'])
    if artifact.part == '花':
        artifact.main_stat = '小生命'
    elif artifact.part == '毛':
        artifact.main_stat = '小攻击'
    elif artifact.part == '头':
        artifact.main_stat = random.choices(
            ['暴击率', '暴击伤害', '大生命', '大攻击', '元素精通', '大防御', '治疗加成'],
            [0.1, 0.1, 0.22, 0.22, 0.05, 0.22, 0.1], k=1)
    elif artifact.part == '杯':
        artifact.main_stat = random.choices(
            ['大攻击', '大防御', '大生命', '元素精通', '物理伤害加成', '火元素伤害加成', '水元素伤害加成',
             '雷元素伤害加成', '冰元素伤害加成', '风元素伤害加成', '岩元素伤害加成', '草元素伤害加成'],
            [0.1917, 0.1917, 0.1917, 0.025, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05], k=1)
    elif artifact.part == '沙':
        artifact.main_stat = random.choices(
            ['大攻击', '大防御', '大生命', '元素充能', '元素精通'],
            [0.2667, 0.2667, 0.2667, 0.1, 0.1], k=1)
    artifact.main_stat = ''.join(str(i) for i in artifact.main_stat) #删除元素外面的列表
    # 看看有几个词条
    if random.random() < 0.2:
        artifact.nsub_stats = 4
    else:
        artifact.nsub_stats = 3
    create_sub_stat(artifact)
    simulate_enhancement(artifact)


# 主程序
if __name__ == '__main__':
    # 创建圣遗物实例
    part = []
    main_stat = ''
    sub_stats = []
    nsub_stats = 0
    val = []
    artifact = Artifact(part=part, main_stat=main_stat, sub_stats=sub_stats, nsub_stats=nsub_stats, val=val)
    create_artifact(artifact)
    Artifact.print_Fin_info(artifact)
    print("双爆分：{:.1f}".format(score(artifact)))
