import pytest

from .pages.main_page import MainPage
from .pages.game_page import ParadiseIslandPage
from .pages.join_us_page import JoinUsPage


@pytest.fixture()
def main_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    yield main_page


@pytest.fixture()
def paradise_island_page(browser):
    pi_page = ParadiseIslandPage(browser)
    pi_page.go_to_site()
    yield pi_page


@pytest.fixture()
def join_us_page(browser):
    ju_page = JoinUsPage(browser)
    ju_page.go_to_site()
    yield ju_page


def test_main_page_games_count(main_page):
    games = main_page.get_games()
    assert len(games) == 7


def test_main_page_games_list(main_page):
    games = main_page.get_games()
    assert set(games) == {'AIRPORT СITY', 'THE TRIBEZ', 'MYSTERY MANOR', 'GUNS OF BOOM',
                          'PARADISE ISLAND 2', 'TREASURE OF TIME', 'MIRRORS OF ALBION'}


def test_main_page_go_to_about_as(main_page):
    main_page.click_on_menu('b912e02c')
    assert main_page.get_active_page_name() == 'ABOUT US'


def test_paradise_island_badges_list(paradise_island_page):
    badges = paradise_island_page.get_badges()
    assert set(badges) == {
        'https://www.microsoft.com/store/apps/9nblggh2tbbg',
        'https://apps.apple.com/app/paradise-island-2-resort-sim/id893555393',
        'https://play.google.com/store/apps/details?id=com.gameinsight.gplay.island2',
        'https://apps.facebook.com/paradiseisland_two/',
        'https://www.amazon.com/Game-Insight-UAB-Paradise-Island/dp/B00V6DUMYE',
        'http://www.samsungapps.com/appquery/appDetail.as?appId=com.gameinsight.samsung.island2',
    }


def test_paradise_island_genre(paradise_island_page):
    assert paradise_island_page.get_genre() == 'Sim/Tycoon'


def test_join_us_void_form(join_us_page):
    join_us_page.submit()
    errors = join_us_page.get_validation_errors()
    assert errors == {
        'application_components_GIFormJoin_accept',
        'application_components_GIFormJoin_email_em_',
        'application_components_GIFormJoin_name_em_',
    }


def test_join_us_invalid_name(join_us_page):
    join_us_page.username = ''
    join_us_page.switch_accept()
    join_us_page.contact_email = 'test@yandex.ru'
    join_us_page.submit()
    errors = join_us_page.get_validation_errors()
    assert errors == {
        'application_components_GIFormJoin_name_em_',
    }


def test_join_us_invalid_email(join_us_page):
    join_us_page.username = 'Jonh Smith'
    join_us_page.switch_accept()
    join_us_page.submit()
    errors = join_us_page.get_validation_errors()
    assert errors == {
        'application_components_GIFormJoin_email_em_',
    }


def test_join_us_invalid_accept(join_us_page):
    join_us_page.username = 'Johnny'
    join_us_page.contact_email = 'test@yandex.ru'
    join_us_page.submit()
    errors = join_us_page.get_validation_errors()
    assert errors == {
        'application_components_GIFormJoin_accept',
    }


def test_join_us_is_valid(join_us_page):
    join_us_page.username = 'Jonh Smith'
    join_us_page.contact_email = 'test@yandex.ru'
    join_us_page.switch_accept()
    join_us_page.submit()
    errors = join_us_page.get_validation_errors()
    assert not errors
