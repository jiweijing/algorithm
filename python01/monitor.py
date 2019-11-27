"""
    设计模式监听模式
    下面是模仿热水器的一种模式描述, 热水器 到一定温度可以让我们享受洗澡的快乐,水烧开了,也可以让我们饮用.
"""
__author__ = 'jiyin'
# @time:2019/11/2719:51

from abc import ABCMeta, abstractmethod
# 引入ABCMeta 和 abstractmethod 来定义抽象类和抽象方法


class Observer(metaclass=ABCMeta):
    """观察者的基类"""
    
    @abstractmethod
    def update(self, observable, object):
        """更新方式"""
        pass


class Observable:
    """被观察者的基类"""
    
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        """通知观察者
            此方法的核心是 被观察者 如热水器 水温上来，可以通过这个方法通知观察者达到对应内容的更新
        """
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    """热水器 战胜寒冬的有力武器"""
    
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        """获取当前温度"""
        return self.__temperature
    
    def setTemperature(self, temperature):
        """赋值当前温度 并且调用 通知观察者方法"""
        self.__temperature = temperature
        print(f"当前温度是:{self.__temperature}C")
        self.notifyObservers()


class WashingMode(Observer):
    """该观察者为 洗澡 意思为 如果想洗澡 观察热水器 水温是否可以洗澡"""
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and 50 <= observable.getTemperature() < 70:
            print("水已经烧好！温度正好,可以用来洗澡了")


class DringkingMode(Observer):
    """该观察者为 饮水 """
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已经烧好了, 可以来饮用了")


if __name__ == '__main__':
    water_heater = WaterHeater()
    dring = DringkingMode()
    wash = WashingMode()
    water_heater.addObserver(dring)
    water_heater.addObserver(wash)
    water_heater.setTemperature(65)
    water_heater.setTemperature(100)
