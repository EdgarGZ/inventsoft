from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
        The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
            Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
            Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
            Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
        The Subject owns some important state and notifies observers when the state
        changes.
    """

    _state: int = None
    _area: str = None
    """
        For simplicity, the Subject's state, essential to all
        subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
        List of subscribers. In real life, the list of subscribers can be stored
        more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
        The subscription management methods.
    """

    def notify(self) -> None:
        """
            Trigger an update in each subscriber.
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self, code: int, area_code: str) -> None:
        """
            Usually, the subscription logic is only a fraction of what a Subject can
            really do. Subjects commonly hold some important business logic, that
            triggers a notification method whenever something important is about to
            happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = code
        self._area = area_code

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
        The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
            Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class AdminObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state = 0:
            print("Notificacion para todos")
        elif subject._state = 1:
            print("Notificacion solo para admin")


class EmployeeObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state = 0:
            print("Notificacion para todos")
        elif subject._state = 2:
            print("Notificacion solo para empleados")