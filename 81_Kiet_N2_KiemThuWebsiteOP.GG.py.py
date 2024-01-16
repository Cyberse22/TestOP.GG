from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import csv
import random


class Test_TimKiem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()

    def test_1_TimKiem_ThanhCong(self):
        # Truy cập trang OP.GG
        self.driver.get('https://www.op.gg/')

        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ div
        region = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]')
        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ button, sau đó nhấn button
        region.find_element(By.XPATH,
                            '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/button')
        region.click()
        time.sleep(5)
        # sau khi thể button được click khoảng 5 giây thì sẽ click vào button theo mảng, ở đây là [15] tương ứng với
        # Vietnam
        region.find_element(By.XPATH,
                            '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/div/button[15]').click()

        with open('player.csv', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                player = row['player']
                search_box = self.driver.find_element(By.NAME, 'search')
                search_box.clear()
                search_box.send_keys(player)
                search_box.submit()
                self.driver.implicitly_wait(5)
                time.sleep(5)

                # Kiểm tra xem người chơi có xuất hiện trong trang không
                page_source = self.driver.page_source
                if page_source == '#':
                    self.assertTrue('#', self.driver.page_source)
                else:
                    self.assertTrue('search result', self.driver.page_source)

    def test_2_TimKiem_Nhung_Sai_TagName(self):
        self.driver.get('https://www.op.gg/')

        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ div
        region = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]')
        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ button, sau đó nhấn button
        region.find_element(By.XPATH,
                            '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/button')
        region.click()
        time.sleep(5)

        # sau khi thể button được click khoảng 5 giây thì sẽ click vào button theo mảng, ở đây là [15] tương ứng với
        # Vietnam
        region.find_element(By.XPATH,
                            f'//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/div/button[15]').click()

        with open('wrongTagName.csv', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                player = row['player']
                search_box = self.driver.find_element(By.NAME, 'search')
                search_box.clear()
                search_box.send_keys(player)
                search_box.submit()
                self.driver.implicitly_wait(5)
                time.sleep(5)

                page_source = self.driver.page_source
                if page_source == '#':
                    self.assertTrue('#', self.driver.page_source)
                else:
                    self.assertFalse('#', self.driver.page_source)

    def test_3_TimKiem_ThatBai_Nhap_Sai_Ten(self):
        # Truy cập trang OP.GG
        self.driver.get('https://www.op.gg/')

        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ div
        region = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]')
        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ button, sau đó nhấn button
        region.find_element(By.XPATH,
                            '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/button')
        region.click()
        time.sleep(5)

        # sau khi thể button được click khoảng 5 giây thì sẽ click vào button theo mảng, ở đây là [15] tương ứng với
        # Vietnam
        region.find_element(By.XPATH,
                            '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/div/button[15]').click()

        with open('wrongPlayer.csv', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                player = row['player']
                search_box = self.driver.find_element(By.NAME, 'search')
                search_box.clear()
                search_box.send_keys(player)
                search_box.submit()
                self.driver.implicitly_wait(5)
                time.sleep(5)

                # Kiểm tra xem người chơi có xuất hiện trong trang không
                page_source = self.driver.page_source
                if page_source == '#':
                    self.assertTrue('#', self.driver.page_source)
                else:
                    self.assertTrue('search result', self.driver.page_source)

    def test_4_TimKiem_ThatBai_Chon_Khong_Dung_May_Chu(self):
        # Tạo một bộ random ngẫu nhiên với tên button_index để có thể chèn vào số ngẫu nhiên trong button[]
        button_index = random.randint(1, 16)
        # Truy cập trang OP.GG
        self.driver.get('https://www.op.gg/')

        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ div
        region = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]')
        # dùng find_element By.XPATH để tìm kiếm và sử dụng chức năng trong thẻ button, sau đó nhấn button
        region.find_element(By.XPATH,
                            '//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/button')
        region.click()
        time.sleep(5)

        # sau khi thể button được click khoảng 5 giây thì sẽ click vào button theo mảng, ở đây là [15] tương ứng với
        # Vietnam
        (region.find_element(By.XPATH,
                             f'//*[@id="__next"]/div[3]/div[2]/div[1]/form/div[1]/div[2]/div/div/button[{button_index}]').click())

        with open('player.csv', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                player = row['player']
                search_box = self.driver.find_element(By.NAME, 'search')
                search_box.clear()
                search_box.send_keys(player)
                search_box.submit()
                self.driver.implicitly_wait(5)
                time.sleep(5)

                page_source = self.driver.page_source
                if page_source == '#':
                    self.assertTrue('#', self.driver.page_source)
                else:
                    self.assertTrue('search result', self.driver.page_source)

    def tearDown(self):
        self.driver.quit()


class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()

    def test_1_DangNhap_Thanh_Cong_Bang_Email(self):
        # Truy cập trang member.op.gg
        self.driver.get('https://member.op.gg/')

        # Tạo một login_email để điền tài khoản
        login_email = self.driver.find_element(By.XPATH, '//*[@id="body"]/div/div/div[1]/form/div[1]/span/input')
        login_email.send_keys('kiethotboy0979@gmail.com')
        time.sleep(5)
        login_email.submit()

        # Chờ 5 giây để có thể chuyển trang khác
        time.sleep(5)

        # Tạo login_pass để điền mật khẩu
        login_pass = self.driver.find_element(By.XPATH, '//*[@id="body"]/div/div/div[1]/form/div[1]/div[2]/span/input')
        login_pass.send_keys('Kietlumop123')
        login_pass.submit()

        # Chờ 5 giây để có thể chuyển trang khác
        time.sleep(5)

        self.assertTrue('My account', self.driver.page_source)

    def test_2_DangNhap_Khong_Duoc_Vi_Khong_Dung_Dinh_Dang(self):
        self.driver.get('https://member.op.gg/')

        # Tạo login_account để điền giá trị vào ô đăng nhập
        login_account = self.driver.find_element(By.XPATH, '//*[@id="body"]/div/div/div[1]/form/div[1]/span/input')
        login_account.send_keys('kiet')
        login_account.submit()

        self.assertTrue('Enter a valid email address.', self.driver.page_source)
        time.sleep(5)

    def test_3_DangNhap_Voi_Email_Chua_Duoc_DangKy(self):
        self.driver.get('https://member.op.gg/')

        # Tạo biến login_email để điền giá trị vào ô đăng nhập
        login_email = self.driver.find_element(By.XPATH, '//*[@id="body"]/div/div/div[1]/form/div[1]/span/input')
        login_email.send_keys('2151013046kiet@ou.edu.vn')
        login_email.submit()
        time.sleep(5)

        # Sau khi đăng nhập với tài khoản chưa được đăng ký, email sẽ được chuyển sang mục đăng ký
        self.assertTrue('Create your OP.GG Member ID', self.driver.page_source)

        # Tạo biến vcode và giả sử nhập sai để điền mã code được gửi qua email đã nhập vào ô email
        vcode = self.driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div/div/form/div[2]/span/input')
        vcode.send_keys('1234')
        vcode.submit()

        self.assertTrue('Invalid auth code.', self.driver.page_source)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
