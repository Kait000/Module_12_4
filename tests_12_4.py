import module_12_4
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        Тестирование метода walk()
        """
        try:
            r_obj = module_12_4.Runner('Roman', -5)
            for i in range(10):
                r_obj.walk()
            self.assertEqual(r_obj.distance, 50, 'Метод walk() не прошел проверку')
            logging.info('test_walk выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=err)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        Тестирование метода run()
        """
        try:
            r_obj = module_12_4.Runner(['Roman', 'Anton'])
            for i in range(10):
                r_obj.run()
            self.assertEqual(r_obj.distance, 100, 'Метод run() не прошел проверку')
            logging.info('test_run выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=err)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
        Тестирование методов run() и walk() на неравенство
        """
        r_obj_1 = module_12_4.Runner('Roman')
        r_obj_2 = module_12_4.Runner('Anton')
        for i in range(10):
            r_obj_1.run()
            r_obj_2.walk()
        self.assertNotEqual(r_obj_1.distance,
                            r_obj_2.distance, 'Методы run() и walk() не прошли проверку на неравенство')


logging.basicConfig(filename='runner_tests.log', encoding='utf-8', filemode='w', level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s")
if __name__ == '__main__':
    unittest.main()
