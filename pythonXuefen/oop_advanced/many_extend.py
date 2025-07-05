#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
多重继承
    在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以
    实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn
'''


class Mammal:
    pass

class RunnableMixIn:
    pass


class CarnivorousMixIn:
    pass
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
