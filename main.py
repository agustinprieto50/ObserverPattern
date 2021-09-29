import store as sub
import client as obs

if __name__ == '__main__':

    obs1 = obs.ConcreteClient('Agustin', 'Prieto')
    subject = sub.ConcreteStore('ipone 6', 0)

    subject.attach(obs1)
    subject.qt = 2