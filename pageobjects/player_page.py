from framework.base_page import BasePage
import time


class PlayerPage(BasePage):

    """
    将该page object所有element都列出来，
    并对每个element都进行命名，即变量名，并写出它的定位方式
    """
    # 进入球员菜单，选择新增球员
    player_tab = "xpath=>//*[@ng-reflect-router-link='/football/player']"  # 导航栏的"球员"菜单//*/ul[@class='li']/li[2]")
    # player_tab = "xpath=>//*/ul[@class='li']/li[2]"
    add_btn = "xpath=>//*[@class='btn btn-default btn-add']"  # 添加球员 按钮
    new_player_btn = "xpath=>//*[@class='text-center'][1]"  # 添加球员时，选择新增球员

    # 进入添加球员填写的二级页面player/add-player
    player_name = "xpath=>//*[@id='name']"  # 球员姓名 # mandatory
    player_id = "xpath=>//*[@id='identity']"  # 球员身份证 ID # mandatory
    player_birthday = "id=>birthday"
    player_gender = "xpath=>//*[@class='dropdown-value']"
    player_female = "xpath=>//*[@class='dropdown-item'][3]"
    player_height = "id=>height"
    player_weight = "id=>weight"
    player_max_hr = "id=>topHeartRate"
    player_basic_hr = "id=>baseHeartRate"
    confirm_submit_btn = "xpath=>//*[@class='btn btn-primary btn-md']"  # 确定提交按钮

    # 修改球员信息
    click_record = "xpath=>//*/tbody/tr[1]"  # 点击球员列表的第一条记录
    edit_btn = "xpath=>//*[@class='edit-icon']"  # 点击编辑图标
    back_players = "xpath=>//*/span[@tabindex=0]"  # 编辑完成后，点击左上角回到球员库(和参数player_tab同样效果)

    # 删除刚刚添加的球员
    delete_player_btn = "xpath=>//*[@class='btn btn-default btn-delete']"  # 删除球员 按钮
    first_checkbox = "xpath=>//*/tbody/tr[1]/td/checkbox[@class='gen-checkbox']"  # 删除列表的第一个球员
    checkbox_all = "xpath=>//*/th/checkbox[@class='gen-checkbox']"  # 全选
    confirm_del_btn = "xpath=>//*[@class='player-header']/button[@class='btn btn-primary']"  # 确定删除按钮
    popup_del_btn = "xpath=>//*[@class='alert-footer']/button[@class='btn btn-primary']"  # 删除弹窗上的确认按钮

    def open_add_player(self):
        self.click(self.player_tab)
        self.click(self.add_btn)
        self.click(self.new_player_btn)
        self.sleep(3)
        print("点击 new player")

    def input_player_info(self, text1, text2, text3, text4, text5):
        js_birthday = "document.getElementById('birthday').removeAttribute('readonly')"  # 去除birthday readonly 属性
        self.type(self.player_name, text1)
        self.type(self.player_id, text2)
        self.driver.execute_script(js_birthday)
        self.type(self.player_birthday, text3)
        self.type(self.player_height, text4)
        self.type(self.player_weight, text5)
        self.click(self.confirm_submit_btn)
        self.take_window_img("PlayerCreated")
        self.sleep(5)
        print("点击提交新增球员")

    def update_player_info(self, text1):
        self.click(self.click_record)
        self.sleep(3)
        self.click(self.edit_btn)
        self.sleep(3)
        self.clear(self.player_name)
        self.type(self.player_name, text1)
        self.click(self.confirm_submit_btn)
        self.take_window_img("PlayerInfoUpdated")
        self.sleep(3)
        print("成功更改球员姓名")

    def del_first_player(self):
        self.click(self.player_tab)
        self.sleep(3)
        self.click(self.add_btn)  # 需要先点击左边的按钮，点击删除球员才有效
        self.click(self.delete_player_btn)
        self.click(self.first_checkbox)
        self.click(self.confirm_del_btn)
        self.take_window_img("PlayerDeleted")
        self.click(self.popup_del_btn)
        print("弹出删除成功的弹窗并点击删除")

    def del_page_players(self):
        self.click(self.player_tab)
        self.sleep(3)
        self.click(self.add_btn)  # 需要先点击左边的按钮，点击删除球员才有效
        self.click(self.delete_player_btn)
        self.click(self.checkbox_all)
        self.click(self.confirm_del_btn)
        self.click(self.popup_del_btn)
        self.take_window_img("APagePlayersDeleted")
        self.sleep(3)
        print("删除一页球员 10 个")

