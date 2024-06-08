import time
import asyncio
from colorama import Fore
from datetime import datetime


class Colorama:
    """
    Xabarlarni turli ranglarda chop etish uchun sinf
    """
    @staticmethod
    def print1(message: str) -> None:
        print(Fore.BLUE + message + Fore.RESET)

    @staticmethod
    def print2(message: str) -> None:
        print(Fore.CYAN + message + Fore.RESET)

    @staticmethod
    def print3(message: str) -> None:
        print(Fore.LIGHTGREEN_EX + message + Fore.RESET)

    @staticmethod
    def print4(message: str) -> None:
        print(Fore.MAGENTA + message + Fore.RESET)

    @staticmethod
    def print_time1(message: str) -> None:
        print(Fore.GREEN + message + Fore.RESET)

    @staticmethod
    def print_time2(message: str) -> None:
        print(Fore.RED + message + Fore.RESET)

    @staticmethod
    def print_time3(message: str) -> None:
        print(Fore.YELLOW + message + Fore.RESET)


class Asyncio:
    """
    Asinxron yaratish va ularni bir vaqtga chiqarish
    """
    @staticmethod
    async def task1() -> None:
        await asyncio.sleep(1)
        Colorama.print1("Task 1 completed")

    @staticmethod
    async def task2() -> None:
        await asyncio.sleep(2)
        Colorama.print3("Task 2 completed")

    @staticmethod
    async def task3() -> None:
        await asyncio.sleep(3)
        Colorama.print2("Task 3 completed")

    @staticmethod
    async def task4() -> None:
        await asyncio.sleep(5)
        Colorama.print4("Task 4 completed")

    @staticmethod
    async def task5() -> None:
        await asyncio.sleep(4)
        Colorama.print1("Task 5 completed")

    @staticmethod
    async def task6() -> None:
        await asyncio.sleep(6)
        Colorama.print3("Task 6 completed")

    @staticmethod
    async def task7() -> None:
        await asyncio.sleep(8)
        Colorama.print2("Task 7 completed")

    @staticmethod
    async def task8() -> None:
        await asyncio.sleep(7)
        Colorama.print4("Task 8 completed")

    @staticmethod
    async def run() -> None:
        """
        Barcha asinxron  bir vaqtda boshlanadi
        """
        await asyncio.gather(
            Asyncio.task1(), Asyncio.task2(), Asyncio.task3(),
            Asyncio.task4(), Asyncio.task5(), Asyncio.task6(),
            Asyncio.task7(), Asyncio.task8()
        )

    @staticmethod
    async def run1() -> None:
        """
        Barcha asinxron chiziqli (ketma ketlikda) bajaradi
        """
        await Asyncio.task1()
        await Asyncio.task2()
        await Asyncio.task3()
        await Asyncio.task4()
        await Asyncio.task6()
        await Asyncio.task7()
        await Asyncio.task8()


class Synchronous:
    """
    Sinxron vazifalarni yaratish va bajarish uchun sinf
    """
    @staticmethod
    def task1() -> None:
        time.sleep(1)
        Colorama.print1("Task 1 completed")

    @staticmethod
    def task2() -> None:
        time.sleep(2)
        Colorama.print3("Task 2 completed")

    @staticmethod
    def task3() -> None:
        time.sleep(3)
        Colorama.print2("Task 3 completed")

    @staticmethod
    def task4() -> None:
        time.sleep(5)
        Colorama.print4("Task 4 completed")

    @staticmethod
    def task5() -> None:
        time.sleep(4)
        Colorama.print2("Task 5 completed")

    @staticmethod
    def task6() -> None:
        time.sleep(6)
        Colorama.print1("Task 6 completed")

    @staticmethod
    def task7() -> None:
        time.sleep(8)
        Colorama.print3("Task 7 completed")

    @staticmethod
    def task8() -> None:
        time.sleep(7)
        Colorama.print4("Task 8 completed")

    @staticmethod
    def run3() -> None:
        """
        Barcha sinxron vazifalarni chiziqli (ketma ketlikda) bajaradi
        """
        Synchronous.task1()
        Synchronous.task2()
        Synchronous.task3()
        Synchronous.task4()
        Synchronous.task5()
        Synchronous.task6()
        Synchronous.task7()
        Synchronous.task8()


class Run:
    """
    Foydalanuvchiga menyu ko'rsatadi va tanlovga qarab tegishli funksiyani ishga tushiradi
    """
    @staticmethod
    def run() -> None:
        tanla: str = input("""
        1.> Asyncio
        2.> Chiziqli Asyncio
        3.> Chiziqli Synchronous
        4.> Back
                >>> : """)

        if tanla == "1":
            Run.main()
        elif tanla == "2":
            Run.main1()
        elif tanla == "3":
            Run.main2()
        elif tanla == "4":
            return
        else:
            Colorama.print_time2("Invalid Input")
        Run.run()

    @staticmethod
    def main() -> None:
        """
        Asinxron vazifalarni bir vaqtda bajarish vaqtini hisoblaydi
        """
        a = datetime.now()
        Colorama.print_time1(f"{a}")
        asyncio.run(Asyncio.run())
        b = datetime.now()
        Colorama.print_time2(f"{b}")
        Colorama.print_time3(f"{b - a}")
        Run.run()

    @staticmethod
    def main1() -> None:
        """
        Asinxron vazifalarni chiziqli (ketma ketlikda) bajarish vaqtini hisoblaydi
        """
        a = datetime.now()
        Colorama.print_time1(f"{a}")
        asyncio.run(Asyncio.run1())
        b = datetime.now()
        Colorama.print_time2(f"{b}")
        Colorama.print_time3(f"{b - a}")
        Run.run()

    @staticmethod
    def main2() -> None:
        """
        Sinxron vazifalarni bajarish vaqtini hisoblaydi
        """
        a = datetime.now()
        Colorama.print_time1(f"{a}")
        Synchronous.run3()
        b = datetime.now()
        Colorama.print_time2(f"{b}")
        Colorama.print_time3(f"{b - a}")
        Run.run()


if __name__ == "__main__":
    Run.run()
