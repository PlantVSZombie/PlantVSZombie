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

僵尸类
创建对象：z=Zombie(行号)
移动 z.move
受到伤害 z.setdamage(受到的伤害)
攻击 z.attack(攻击对象的列表)
子弹类
创建对象
bullet=Bullet(plant)
bullet.attack(攻击对象的列表)
bullet.update()

植物类
plant=PeaShooter(列号，行号)
plant.shot()射子弹
plant.setDamage（damage）
plant.isAlive（）是否存活

Zone区域类
getIndex由坐标转化为草坪坐标
getGridPos草坪坐标转化为像素坐标
