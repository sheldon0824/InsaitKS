from framework.base_page import BasePage
import os.path

class TeamPage(BasePage):

    """Enter Team tab page"""
    team_tab = "xpath=>//*[@ng-reflect-router-link='/football/team']"  # team_tab
    add_team_btn = "xpath=>//*[@class='header team-adder clearfix']/button[1]"  # 点击新增球队 按钮

    """Pop-up New Team window and input info"""
    team_name = "id=>teamName"
    home_jersey = "xpath=>//*[@id='colorHome']/div"
    home_jersey_color = "xpath=>//*[@class='dropdown-menu color-ul clear-fix']/li[9]"  # select 9th color
    away_jersey = "xpath=>//*[@id='colorGuest']/div"
    away_jersey_color = "xpath=>//*[@id='colorGuest']/div/ul/li[1]"  # select 1st color
    speed_section = "xpath=>//*[@class='speed-wrapper clearfix']/div/label[2]"  # checked on mid-speed option
    confirm_btn = "xpath=>//*[@class='btn btn-primary btn-md']"  # submit data by clicking confirm button

    """open bulk import players on team page"""
    first_team = "xpath=>//*/div[@class='team pull-left']"  # click the first record on team list
    player_nav = "xpath=>//*[@class='nav']/ul/li[2]"  # switch to player navigation
    add_player_btn = "xpath=>//*[@class='btn btn-default btn-add']"
    bulk_imp_btn = "xpath=>//*[@class='text-center'][3]"
    import_panel = "id=>drop-zone"  # 点击上传excel的界面
    close_import_panel = "xpath=>//*/p[@class='batch-importer-header']/small"

    """delete team"""
    team_del_btn = "xpath=>//*[@id='team-content']/div/button[2]"  # 删除按钮进入删除界面
    del_1st_team = "xpath=>//*[@class='team pull-left isDelete'][1]"  # 删除第一支球队
    # 下面是弹窗删除确认按钮，这里由于界面上存在太多相同的元素，所以要一直往上一级定位
    pop_up_del_btn = "xpath=>//*[@id='team-content']/app-alert/div/div/footer/button[1]"

    def create_team(self, text1):
        self.click(self.team_tab)
        self.sleep(3)
        self.click(self.add_team_btn)
        self.type(self.team_name, text1)
        self.click(self.home_jersey)
        self.click(self.home_jersey_color)
        self.click(self.away_jersey)
        self.click(self.away_jersey_color)
        self.click(self.speed_section)
        self.take_window_img("TeamCreated")
        self.click(self.confirm_btn)
        self.sleep(3)

    def bulk_in_team(self, excel_file):
        self.click(self.team_tab)
        self.sleep(2)
        self.click(self.first_team)
        self.sleep(3)
        self.click(self.player_nav)
        self.sleep(3)
        self.click(self.add_player_btn)
        self.click(self.bulk_imp_btn)
        self.type(self.import_panel, excel_file)
        self.sleep(3)
        self.take_window_img("PlayersImported")
        self.click(self.close_import_panel)
        self.sleep(3)

    def del_team(self):
        self.click(self.team_tab)
        self.click(self.team_del_btn)
        self.click(self.del_1st_team)
        self.click(self.pop_up_del_btn)
        self.take_window_img("TeamDeleted")






