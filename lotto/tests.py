from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test case', text='selected numbers')
        g.generate() #GuessNumbers 클래스의 generate 함수를 실행
        print(g.update_date)
        print(g.lottos)

        #실제 Test case(OK or FAILED)
        #default로 6개로 숫자x5개 set이 생성되어야 함
        self.assertTrue(len(g.lottos) > 20)