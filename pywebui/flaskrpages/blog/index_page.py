from selenium.webdriver.common.by import By


class IndexPage:

    URL = 'http://localhost:80/'
    REGISTER_ANCHOR = (By.XPATH, '//a[contains(text(), "Register")]')
    LOGIN_ANCHOR = (By.XPATH, '//a[contains(text(), "Log In")]')
    LOGOUT_ANCHOR = (By.XPATH, '//a[contains(text(), "Log Out")]')
    POSTS_HEADER = (By.XPATH, '//h1[contains(text(), "Posts")]')
    NEW_ANCHOR = (By.XPATH, '//a[contains(text(), "New")]')
    POSTS = (By.XPATH, '//article[@class="post"]')

    @classmethod
    def POST_BY_INDEX(cls, index):
        """
        :param index: 1,2,3, ...
        """
        xpath = f"//article[@class='post'][{index}])]"
        return By.XPATH, xpath

    @classmethod
    def POST_BY_ID(cls, id):
        xpath = f"//article[@class='post']/header/a[starts-with(@href, '/{id}')]/ancestor::article"
        return By.XPATH, xpath

    def __init__(self, browser):
         self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def open_register_page(self):
        register_link = self.browser.find_element(*self.REGISTER_ANCHOR)
        register_link.click()

    def open_login_page(self):
        login_link = self.browser.find_element(*self.LOGIN_ANCHOR)
        login_link.click()

    def posts_header_exists(self):
        posts_header = self.browser.find_element(*self.POSTS_HEADER)
        return posts_header is not None

    def open_create_post_page(self):
        new_link = self.browser.find_element(*self.NEW_ANCHOR)
        new_link.click()

    def get_posts_count(self):
        posts = self.browser.find_element(*self.POSTS)
        return len(posts) if posts is not None else 0