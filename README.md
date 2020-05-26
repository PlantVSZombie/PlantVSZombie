# PlantVSZombie
##项目思路
采用pygame，分模块开发
## 第一次分工
已分工：
刘宗游：Plant类+Bullet类
郑祺琛：Zombie类
郑汉亚：Sun+Car类
葛伟平：选卡界面

未分工：
Controller类
游戏界面

## 教程
 碰撞检测实例 教程 https://blog.csdn.net/sinat_39013092/article/details/81869401
 面向对象编程 https://www.liaoxuefeng.com/wiki/1016959663602400/1017495723838528
 单元测试教程 https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936

## 第二次分工
刘宗游：写一部分Controller类   
郑祺琛：完善Zombie类  
郑汉亚：完善Sun和Car类  
葛伟平：完善地图界面  
要求：简单为主，实现基本功能即可（植物向日葵+豌豆射手，僵尸普通僵尸。当然如果你是时间管理大师想多写那随便你怎么躁）。赶快做完写实验报告，之后搞软工课设了哈哈哈

### 僵尸类
创建对象：z=Zombie(行号)
移动 z.move
受到伤害 z.setdamage(受到的伤害)
攻击 z.attack(攻击对象的列表)
### 子弹类
创建对象 bullet=Bullet(plant)
bullet.attack(攻击对象的列表)
bullet.update()

### 植物类
plant=PeaShooter(列号，行号)
plant.shot()射子弹
plant.setDamage（damage）
plant.isAlive（）是否存活

### Zone区域类
getIndex由坐标转化为草坪坐标
getGridPos草坪坐标转化为像素坐标

### Car类
1. Car.CreateCarAtRow(i)创建第i行的车
2. car.check(zombieList) #检测是否有碰撞
3. car.draw(screen) #绘图
4. car.isRUN_OUT_SCREEN(): #小车是否跑出去了
示例程序：

```python
# 创建
    cars = []
    for i in range(5):
        car = Car.CreateCarAtRow(i)  # 第i行的车 对不齐是getGridPos函数可能有点问题
        cars.append(car)
#碰撞检测+小车移动
    for car in cars:
        car.check(zombieList) #检测是否有碰撞
        car.update() #更新状态
        car.draw(screen) #绘图
        if car.isRUN_OUT_SCREEN(): #小车跑出去了
            cars.remove(car)
```
### Sun类
1. sun = Sun(200, 0，3) #初始X，Y坐标，速度（可省略）
2. sun.SetLineDestination(200)  # 直线下降 参数：目标Y坐标 白天自动生成的
3. sun.SetArcDestination(250, 200)  # 斜着跑 参数：目标XY坐标 向日葵生成的
4. sun.update() #更新状态
5. sun.isAlive() #是否超时没点击
6. sun.draw(screen) #绘图
7. sun.isClicked(mouse_click, (x, y))是否被点击
```python
#管理所有太阳
    suns=[]
    sun_index=0
    sun_max=20 #控制多久产生一个太阳
#创建太阳
    if sun_index>=sun_max:
        sun = Sun(random.randint(200,800), 0,5) #初始X，Y坐标，速度（可省略）
        sun.SetLineDestination(random.randint(50,500))  # 直线下降 参数：目标Y坐标 白天自动生成的
        suns.append(sun)
        sun_index=0
    else:
        sun_index+=1
#点击判断
    x, y = pygame.mouse.get_pos()
    mouse_click, _, _ = pygame.mouse.get_pressed()

    for sun in suns:
        sun.update() #更新状态
        if sun.isAlive():
            sun.draw(screen)
            if sun.isClicked(mouse_click, (x, y)):
                print("阳光+10")
        else:
            suns.remove(sun)
```
### Menubar类
1.menu=Menubar(x,y,card_list,sun_value) #左上角坐标，拥有的卡片列表，初始太阳值
2.menu.incSunValue(value) #增加太阳值
3.menu.decSunValue(value) #减少太阳值
4.menu.checkCardChosen(mouse_click,mouse_pos) #检查拥有卡片是否被点击，若有则返回该卡片
