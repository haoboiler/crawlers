from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os,time
import random



class CBCrawler(object):
    
    def __init__(self, web_address = 'http://www.crunchbase.com/login', username = '', password = '') -> None:
        super().__init__()
        self.web_address = web_address
        self.username = username
        self.password = password
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(self.web_address)
    
        
    def sleep(self):
        i = random.randint(1, 8)
        time.sleep(i)
        
        
    def login(self):
        self.browser.implicitly_wait(10)
        #browser.find_element_by_class_name('mat-input-element mat-form-field-autofill-control ng-tns-c61-7 ng-untouched ng-pristine cdk-text-field-autofill-monitored ng-invalid').send_keys(self.username)
        print('获取用户名')
        user_name_tag = self.browser.find_element_by_id('mat-input-1') #用户名   
        user_name_tag.send_keys(self.username)
        self.sleep()
        print('获取密码')
        password_tag = self.browser.find_element_by_id('mat-input-2') #密码
        password_tag.send_keys(self.password) 
        self.sleep()
        print('登陆')
        button_tag = self.browser.find_element_by_css_selector('#mat-tab-content-0-0 > div > login > form > button') #用户名
        button_tag.click()
        self.sleep()
        
    def AdvanceSearch(self, page):
        self.browser.implicitly_wait(10)
        self.browser.switch_to_window(self.browser.window_handles[-1]) #切换句柄
        class_choose = self.browser.find_element_by_css_selector('body > chrome > div > app-header > div.header-contents.mat-elevation-z3.layout-row.layout-align-space-between-center.logged-in > div.hide-print.flex-noshrink.layout-row.layout-align-space-between-stretch.cb-height-100 > nav-menu > button > span.mat-button-wrapper > nav-action-item-header-layout')
        class_choose.click()
        self.browser.implicitly_wait(10)
        self.sleep()
        
        people_button = self.browser.find_element_by_css_selector('#mat-menu-panel-0 > div > div > mat-nav-list > nav-groups > nav-action-item:nth-child(6) > nav-menu-action-item > a > nav-action-item-layout') #到people的按钮
        people_button.click()
        self.browser.implicitly_wait(10)
        self.sleep()
        #switch to people page
        self.browser.switch_to_window((self.browser.window_handles[-1]))
        query_button = self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > discover > page-layout > div > div > div.advanced-search-container.layout-row > section.filters > div.filter-groups > button')
        query_button.click()
        self.sleep()
        
        self.people_filter_input(page)
        
    def people_filter_input(self, start_i):
        #switch to people page
        self.browser.switch_to_window((self.browser.window_handles[-1]))
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > search > page-layout > div > div > form > div.filters-outer-container.flex-nogrow.cb-overflow-auto.cb-background-white > div > filters > query-item-add > div > button').click()
        self.sleep()
        self.browser.implicitly_wait(5)

        #按下rank按钮
        print('按下rank')
        rank_column = self.browser.find_element_by_css_selector('#mat-dialog-0 > query-item-drill-panel > div > dialog-layout > div > mat-dialog-content > div > div > div.heightWrapper > div > div:nth-child(1) > mat-nav-list > mat-list-item:nth-child(6) > div > div.cb-width-100.layout-row.layout-align-space-between-center > label-with-info > div')
        rank_column.click()
        self.browser.implicitly_wait(10)
        self.sleep()
        
        #选择CB rank
        rank = self.browser.find_element_by_css_selector('#mat-dialog-0 > query-item-drill-panel > div > dialog-layout > div > mat-dialog-content > div > div > div.heightWrapper > div > div:nth-child(2) > mat-nav-list > mat-list-item:nth-child(1) > div > label-with-info > div')
        rank.click()
        self.sleep()
                
        #
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > search > page-layout > div > div > form > div.filters-outer-container.flex-nogrow.cb-overflow-auto.cb-background-white > div > filters > div > div > div > query-item > div > predicate > div > div.fieldWrapper.flex-none > query-item-add > div > button').click()
        self.sleep()
        self.browser.implicitly_wait(5)

        #按下rank按钮
        print('按下rank')
        rank_column = self.browser.find_element_by_css_selector('#mat-dialog-1 > query-item-drill-panel > div > dialog-layout > div > mat-dialog-content > div > div > div.heightWrapper > div > div:nth-child(1) > mat-nav-list > mat-list-item:nth-child(6) > div > div.cb-width-100.layout-row.layout-align-space-between-center > label-with-info > div')
        rank_column.click()
        self.browser.implicitly_wait(10)
        self.sleep()
        
        #选择CB rank
        rank = self.browser.find_element_by_css_selector('#mat-dialog-1 > query-item-drill-panel > div > dialog-layout > div > mat-dialog-content > div > div > div.heightWrapper > div > div:nth-child(2) > mat-nav-list > mat-list-item:nth-child(1) > div > label-with-info > div')
        rank.click()
        self.sleep()
        
        # 选择 less than
        self.browser.find_element_by_css_selector('#mat-select-4').click()
        self.sleep()
        self.browser.find_element_by_css_selector('#mat-option-11').click()
        self.sleep()
        
        for i in range(start_i,2000):
            print(i)
            self.enter_and_download(i*800, (i+1)*800)
            #self.enter_and_download(i*1000+501, i*1000+999)
            self.sleep()
    
    def enter_and_download(self, min, max):        
        # 输入rank
        rank_input = self.browser.find_element_by_css_selector('#mat-input-17')
        rank_input.click()
        for i in range(9):
            rank_input.send_keys(Keys.BACK_SPACE)
        print('input %s' % max)
        rank_input.send_keys(min)
        self.browser.implicitly_wait(10)
        
        
        self.sleep()        
        # 输入rank
        rank_input = self.browser.find_element_by_css_selector('#mat-input-19')
        rank_input.click()
        for i in range(9):
            rank_input.send_keys(Keys.BACK_SPACE)
        print('input %s' % max)
        rank_input.send_keys(max)
        self.browser.implicitly_wait(10)
        self.sleep()
                
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > search > page-layout > div > div > form > div.cb-flex-at-least-50.layout-column > results > div > div > div.cb-background-white.cb-padding-small-vertical.flex-none.layout-column.layout-align-center-stretch.layout-gt-xs-row.layout-align-gt-xs-start-center > div > button').click()
        self.sleep()
        
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > search > page-layout > div > div > form > div.cb-flex-at-least-50.layout-column > results > div > div > div.cb-background-white.cb-padding-small-vertical.flex-none.layout-column.layout-align-center-stretch.layout-gt-xs-row.layout-align-gt-xs-start-center > div > div > div > export-csv-button > button').click()
        self.sleep()
        
    def get_lists_search_company(self):
        class_choose = self.browser.find_element_by_css_selector('body > chrome > div > app-header > div.header-contents.mat-elevation-z3.layout-row.layout-align-space-between-center.logged-in > div.hide-print.flex-noshrink.layout-row.layout-align-space-between-stretch.cb-height-100 > div > logged-in-nav-menus > nav-menu:nth-child(1) > button > span.mat-button-wrapper > nav-action-item-header-layout > div')
        class_choose.click()
        self.browser.implicitly_wait(10)
        
        save_searches_choose = self.browser.find_element_by_css_selector('#mat-menu-panel-1 > div > div > mat-nav-list > nav-groups > nav-action-item:nth-child(3) > nav-menu-action-item > a > nav-action-item-layout > span')
        save_searches_choose.click()
        self.browser.implicitly_wait(10)
        
        self.browser.switch_to_window((self.browser.window_handles[-1]))
        
        self.browser.implicitly_wait(10)
        company_download_button = self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > lists > page-layout > div > div > div.cb-relative.flex.ng-star-inserted > sheet-grid > div > div > grid-body > div > grid-row:nth-child(1) > grid-cell:nth-child(2) > div > a')
        company_download_button.click()
        print('end company 1')

    def get_lists_search_rounds(self):
        class_choose = self.browser.find_element_by_css_selector('body > chrome > div > app-header > div.header-contents.mat-elevation-z3.layout-row.layout-align-space-between-center.logged-in > div.hide-print.flex-noshrink.layout-row.layout-align-space-between-stretch.cb-height-100 > div > logged-in-nav-menus > nav-menu:nth-child(1) > button > span.mat-button-wrapper > nav-action-item-header-layout > div')
        class_choose.click()
        self.browser.implicitly_wait(10)
        
        save_searches_choose = self.browser.find_element_by_css_selector('#mat-menu-panel-1 > div > div > mat-nav-list > nav-groups > nav-action-item:nth-child(3) > nav-menu-action-item > a > nav-action-item-layout > span')
        save_searches_choose.click()
        self.browser.implicitly_wait(10)
        
        self.browser.switch_to_window((self.browser.window_handles[-1]))
        
        self.browser.implicitly_wait(10)
        company_download_button = self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > lists > page-layout > div > div > div.cb-relative.flex.ng-star-inserted > sheet-grid > div > div > grid-body > div > grid-row:nth-child(4) > grid-cell:nth-child(2) > div > a')
        company_download_button.click()
        print('end round 1')
            
    def company_filter_input(self):
        #第一个rank按钮
        self.browser.switch_to_window((self.browser.window_handles[-1]))
        first_filter_button = self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > list-search > page-layout > div > div > form > div.flex-nogrow.cb-overflow-auto.ng-star-inserted > filters > div > div > div:nth-child(3) > query-item > div > subquery > div > div.fieldWrapper.flex-none > query-item-add > div > button > span.mat-button-wrapper > div > span')
        first_filter_button.click()
        self.sleep()
        self.browser.implicitly_wait(5)
        
        #按下rank
        rank_button = self.browser.find_element_by_css_selector('#mat-dialog-0 > query-item-drill-panel > div > dialog-layout > div > mat-dialog-content > div > div > div.heightWrapper > div > div:nth-child(1) > mat-nav-list > mat-list-item:nth-child(13) > div > div.cb-width-100.layout-row.layout-align-space-between-center')
        rank_button.click()
        self.sleep()
        self.browser.implicitly_wait(5)
        
        #按下cb rank
        rank_button = self.browser.find_element_by_css_selector('#mat-dialog-0 > query-item-drill-panel > div > dialog-layout > div > mat-dialog-content > div > div > div.heightWrapper > div > div:nth-child(2) > mat-nav-list > mat-list-item:nth-child(2) > div > label-with-info > div > span.cb-overflow-ellipsis.flex-nogrow.label')
        rank_button.click()
        self.sleep()
        self.browser.implicitly_wait(5)


    def CompanyAdvanceSearch(self, start_i):
        for i in range(start_i,2000):
            print(i)
            self.enter_and_download_company(i*2000, (i+1)*2000)
            #self.enter_and_download(i*1000+501, i*1000+999)
            self.sleep()        
      
    def enter_and_download_company(self, min, max):
        # 输入rank
        rank_input = self.browser.find_element_by_css_selector('#mat-input-11')
        rank_input.click()
        for i in range(9):
            rank_input.send_keys(Keys.BACK_SPACE)
        print('input %s' % max)
        rank_input.send_keys(min)
        self.browser.implicitly_wait(10)
            
        self.sleep()        
        # 输入rank
        rank_input = self.browser.find_element_by_css_selector('#mat-input-12')
        rank_input.click()
        for i in range(9):
            rank_input.send_keys(Keys.BACK_SPACE)
        print('input %s' % max)
        rank_input.send_keys(max)
        self.browser.implicitly_wait(10)
        self.sleep()
                
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > list-search > page-layout > div > div > form > div.cb-flex-at-least-50.layout-column.cb-overflow-auto > results > div > div > div.cb-background-white.cb-padding-small-vertical.flex-none.layout-column.layout-align-center-stretch.layout-gt-xs-row.layout-align-gt-xs-start-center > div > button').click()
        self.sleep()
        
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > list-search > page-layout > div > div > form > div.cb-flex-at-least-50.layout-column.cb-overflow-auto > results > div > div > div.cb-background-white.cb-padding-small-vertical.flex-none.layout-column.layout-align-center-stretch.layout-gt-xs-row.layout-align-gt-xs-start-center > div > div > div > export-csv-button > button').click()
        self.sleep()
        
        #self.browser.implicitly_wait(5)
        #self.browser.find_element_by_css_selector('#mat-dialog-2 > confirmation-dialog > dialog-layout > div > mat-dialog-actions > div > button.mat-focus-indicator.cb-text-transform-upper.mat-raised-button.mat-button-base.mat-primary > span.mat-button-wrapper').click()
        #self.sleep()                                   
    
    def RoundsAdvanceSearch(self, start_i):
        for i in range(start_i,8000):
            print(i)
            self.enter_and_download_rounds(i*400, (i+1)*400)
            #self.enter_and_download(i*1000+501, i*1000+999)
            self.sleep()        
      
    def enter_and_download_rounds(self, min, max):
        # 输入rank
        rank_input = self.browser.find_element_by_css_selector('#mat-input-8')
        rank_input.click()
        for i in range(9):
            rank_input.send_keys(Keys.BACK_SPACE)
        print('input %s' % max)
        rank_input.send_keys(min)
        self.browser.implicitly_wait(10)
            
        self.sleep()        
        # 输入rank
        rank_input = self.browser.find_element_by_css_selector('#mat-input-9')
        rank_input.click()
        for i in range(9):
            rank_input.send_keys(Keys.BACK_SPACE)
        print('input %s' % max)
        rank_input.send_keys(max)
        self.browser.implicitly_wait(10)
        self.sleep()
                
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > list-search > page-layout > div > div > form > div.results-container > results > div > div > div.cb-background-white.cb-padding-small-vertical.flex-none.layout-column.layout-align-center-stretch.layout-gt-xs-row.layout-align-gt-xs-start-center > div > button').click()
        self.sleep()
        
        self.browser.find_element_by_css_selector('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > list-search > page-layout > div > div > form > div.results-container > results > div > div > div.cb-background-white.cb-padding-small-vertical.flex-none.layout-column.layout-align-center-stretch.layout-gt-xs-row.layout-align-gt-xs-start-center > div > div > div > export-csv-button > button > span.mat-button-wrapper > label-with-icon > span').click()
        self.sleep()
        
        #self.browser.implicitly_wait(5)
        #self.browser.find_element_by_css_selector('#mat-dialog-2 > confirmation-dialog > dialog-layout > div > mat-dialog-actions > div > button.mat-focus-indicator.cb-text-transform-upper.mat-raised-button.mat-button-base.mat-primary > span.mat-button-wrapper').click()
        #self.sleep()            
    
    def run(self):
        while(True):
            input_str = input()
            if input_str == 'login':
                try:
                    print('login')
                    self.login()
                except Exception as e:
                    print(e)
                    continue
            if input_str == 'company':
                try:
                    print('company')
                    self.get_lists_search_company()()
                    self.company_filter_input()
                except Exception as e:
                    print(e)
                    continue
            if input_str == 'round':
                try:
                    print('round')
                    self.get_lists_search_rounds()
                    self.company_filter_input()
                except Exception as e:
                    print(e)
                    continue
            if input_str.isdigit():
                try:
                    print('adv search')
                    #self.AdvanceSearch(int(input_str))
                    #self.CompanyAdvanceSearch(int(input_str))
                    self.RoundsAdvanceSearch(int(input_str))
                except Exception as e:
                    print(e)
                    continue
                
            if input_str == 'exit':
                break
        self.browser.close()
        
        
        